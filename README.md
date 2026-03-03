# Yaml-model-files-for-LMS
Yaml model files for LMS
Quickly did these up. They contain all/most quants currently available (03/03/2026) including lmstudio-community but not MLX quants. Unless the model is new then there is little reason these should be updated more than once every 3 or so months but I likely won't update past 3 months.

To add a model not in these  put uder base (at th top for quick locating and fill out his 9Note: readme doesn't show the appropriate verison in preview:
````
  - key: Insert Publisher/Insert Model  (e.g. AesSedai/Qwen3.5-122B-A10B-GGUF (copy from model page))

    sources:
    
      - type: huggingface
      
        user: Insert Publisher
        
        repo: Insert Model``

````
Put under

Windows: ~\Users\\%USERNAME%\\.lmstudio\\hub\\models\\%Company%\\%Model%

Linux/Mac: ~/.lmstudio/hub/models/%Company%/%Model%

Make sure that the file is under the correct company and model

Thanks Yorkie, Roxxus and in part Lithium
