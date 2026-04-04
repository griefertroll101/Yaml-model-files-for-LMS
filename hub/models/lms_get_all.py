#!/usr/bin/env python3
"""
LMS Get All Models
------------------
Downloads all griefertroll-yaml model configs from LM Studio's registry.
Each 'lms get' command fetches the model.yaml for that model.

Usage:
    python lms_get_all.py          # run all (blocks downloads over 100 MB)
    python lms_get_all.py --yes    # accept all prompts (no size limit)
    python lms_get_all.py --dry    # preview commands without running
"""

import subprocess
import sys
import time
import os
import re

# ============================================================================
# CONFIG
# ============================================================================

# Maximum download size allowed in MB — process is killed if lms tries
# to download more than this. Only applies in default mode (not --yes).
MAX_DOWNLOAD_MB = 100

# LM Studio models directory — adjust if yours is different
LMS_MODELS_DIR = os.path.expanduser("~/.lmstudio/hub/models")

# ============================================================================
# HELPERS
# ============================================================================


def parse_size_mb(text):
    """Extract download size in MB from lms output.
    Matches lines like 'About to download 38.42 GB.' or size hints
    like '- 38.42 GB' at the end of a line.
    Returns size in MB, or 0 if not found."""

    # Match "About to download 38.42 GB."
    m = re.search(r"About to download\s+([\d.]+)\s*(GB|MB|KB)", text, re.IGNORECASE)
    if not m:
        # Match "- 38.42 GB" at end of line (the per-file size hint)
        m = re.search(r"-\s+([\d.]+)\s*(GB|MB|KB)\s*$", text, re.IGNORECASE)
    if not m:
        return 0

    value = float(m.group(1))
    unit = m.group(2).upper()
    if unit == "GB":
        return value * 1000
    elif unit == "MB":
        return value
    elif unit == "KB":
        return value / 1000
    return 0


def run_lms_get(model, accept_all=False):
    """Run 'lms get' for a single model.

    Monitors stdout line-by-line. If a line indicates a download larger
    than MAX_DOWNLOAD_MB, the process is killed immediately.

    When accept_all is True, no size checking is done.

    Returns (success, reason)."""

    try:
        proc = subprocess.Popen(
            ["lms", "get", model],
            stdin=None if accept_all else subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    except FileNotFoundError:
        return False, "lms command not found"

    killed = False
    kill_reason = ""

    try:
        # Read output line-by-line so we can react to size info
        for line in proc.stdout:
            line = line.rstrip("\n")
            print(f"  {line}")

            # Skip size checks if --yes was passed
            if accept_all:
                continue

            # Check if this line mentions a download size over the limit
            size_mb = parse_size_mb(line)
            if size_mb > MAX_DOWNLOAD_MB:
                kill_reason = f"{size_mb:.0f} MB exceeds {MAX_DOWNLOAD_MB} MB limit"
                print(f"  BLOCKED — {kill_reason}, killing process")
                proc.kill()
                killed = True
                break

        proc.wait(timeout=300)

    except subprocess.TimeoutExpired:
        proc.kill()
        return False, "timed out"

    if killed:
        return False, f"blocked ({kill_reason})"

    if proc.returncode != 0:
        return False, f"exit code {proc.returncode}"

    return True, "ok"


def cleanup_large_files(model_id):
    """Safety net: check the model's folder for any files over the limit
    and delete them. Returns list of removed filenames."""

    model_dir = os.path.join(LMS_MODELS_DIR, model_id.replace("/", os.sep))
    if not os.path.isdir(model_dir):
        return []

    max_bytes = MAX_DOWNLOAD_MB * 1_000_000
    removed = []
    for root, dirs, files in os.walk(model_dir):
        for fname in files:
            fpath = os.path.join(root, fname)
            try:
                size = os.path.getsize(fpath)
                if size > max_bytes:
                    os.remove(fpath)
                    size_mb = size / 1_000_000
                    print(f"  REMOVED {fname} ({size_mb:.1f} MB)")
                    removed.append(fname)
            except OSError:
                pass
    return removed


# ============================================================================
# MODEL LIST
# All rintaro/ models to download via 'lms get'
# ============================================================================

MODELS = [
    # --- Seed OSS (ByteDance) ---
    "rintaro/seed-oss-36b",

    # --- Gemma 4 (Google) ---
    "rintaro/gemma-4-26b-a4b",
    "rintaro/gemma-4-31b",
    "rintaro/gemma-4-e2b",
    "rintaro/gemma-4-e4b",

    # --- MiniMax ---
    "rintaro/minimax-m2.5",

    # --- Mistral ---
    "rintaro/mistral-small-4",

    # --- Hermes (NousResearch) ---
    "rintaro/hermes-4-14b",
    "rintaro/hermes-4-405b",
    "rintaro/hermes-4-70b",
    "rintaro/hermes-4.3-36b",

    # --- Nemotron 3 (NVIDIA) ---
    "rintaro/nemotron-3-nano-4b",
    "rintaro/nemotron-3-nano",
    "rintaro/nemotron-3-super",

    # --- GPT-OSS (OpenAI) ---
    "rintaro/gpt-oss-120b",
    "rintaro/gpt-oss-20b",

    # --- Qwen 3.5 (Alibaba) ---
    "rintaro/qwen3.5-122b-a10b",
    "rintaro/qwen3.5-27b",
    "rintaro/qwen3.5-35b-a3b",
    "rintaro/qwen3.5-397b-a17b",
    "rintaro/qwen3.5-4b",
    "rintaro/qwen3.5-9b",

    # --- GLM (Zhipu AI) ---
    "rintaro/glm-4.5-air",
    "rintaro/glm-4.7-flash",
]


# ============================================================================
# RUNNER
# Executes each 'lms get' command and tracks results
# ============================================================================

def main():
    # Check for flags
    dry_run = "--dry" in sys.argv
    accept_all = "--yes" in sys.argv

    if dry_run:
        print("=== DRY RUN — commands that would be executed ===\n")
        for model in MODELS:
            print(f"  lms get {model}")
        print(f"\nTotal: {len(MODELS)} models")
        return

    if accept_all:
        mode = "ACCEPT ALL (no size limit)"
    else:
        mode = f"CONFIG ONLY (blocking downloads over {MAX_DOWNLOAD_MB} MB)"
    print(f"Fetching {len(MODELS)} models — {mode}\n")

    succeeded = []
    failed = []

    for i, model in enumerate(MODELS, 1):
        # Show progress
        print(f"\n[{i}/{len(MODELS)}] lms get {model}")

        ok, reason = run_lms_get(model, accept_all=accept_all)

        if ok:
            succeeded.append(model)
        else:
            failed.append((model, reason))
            # If lms isn't installed, stop immediately
            if "not found" in reason:
                print("\nMake sure LM Studio CLI is installed and on your PATH.")
                sys.exit(1)

        # Safety net: remove any oversized files that slipped through
        if not accept_all:
            cleanup_large_files(model)

        # Small delay between requests
        time.sleep(0.5)

    # ========================================================================
    # SUMMARY
    # ========================================================================

    print(f"\n{'=' * 50}")
    print(f"Done: {len(succeeded)} OK, {len(failed)} failed")

    if failed:
        print("\nFailed models:")
        for model, reason in failed:
            print(f"  {model} — {reason}")


if __name__ == "__main__":
    main()
