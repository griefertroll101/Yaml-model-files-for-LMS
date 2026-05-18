# Issue regarding some models
A couple models but overall 90% have no problems. Problem models still work but just double models because LMS BS implementation.
# Yaml Model Files For LMS
Note: This is maintained by GrieferTroll in the LM Studio discord. Please do not bother Yags or Yorkie they have better things to do. DM me if an issue is here or use the issues tab here.

Plan to add MLX but may be a week or 2 before I do.

Quickly did these up. They contain all/most quants currently available (19th of May 2026) including lmstudio-community but not MLX quants. Now able to update easily, so every month likely or when a new model comes out it will be getting done daily/weekly

## Models Done
| Google Gemma 4 E2B, E4B, 26B-A4B, 31B | Qwen 3  4B, 9B, 30B-A3B, 235B-A22B | Qwen 3.5 4B, 9B, 35B-A3B, 122B-A10B, 397B-A17B | Qwen 3.6 27B, 35B-A3B | OpenAI GPT-OSS 20B, 120B | Z.ai GLM 5.1, 5, 4.7 Flash, 4.5 Air | NVIDIA Nemotron 3 4B, Nano 30B, Cascade-2-30B-A3B, Super | ByteDance Seed-OSS 36B | NousResearch Hermes 4 14B, 70B, 405B, Hermes 4.3 36B | MistralAI Mistral Small 4 |

Soon to be added: Other GLM models

## Install All (Recommended)
Click on the green code at the top of the page and download the zip. Put that zip in the .lmstudio folder and extract all. Open the extracted folder and drag/cut/copy the hub folder into .lmstudio. If prompted Do you want to replace... select yes. 

Windows Location: C:\\Users\\%Username%\\.lmstudio

2nd Windows Location: C:\\Users\\.cache\\%Username%\\.lmstudio

Linux/Mac Location: ~/.lmstudio

An issue you may run into is that your models may duplicate. If this happens go to C:\\Users\\%Username%\\.lmstudio\models choose the provider (will be in model tab under publisher) then drag the folder with the name of the duplicated model out of the publisher folder then back in. 

````
%Username% = Name of the user on the PC e.g greg
````

If you do not know the username for the PC then follow the folders one by one i.e start in the Local Disk (C:) then click on the users folder then select the folder that doesn't have the name Default or Public. Once you have selected the %username% folder .lmstudio should be among the folders in that folder.

## Individually

If you want to install model.yaml individually then put under

Windows Location: C:\\Users\\%Username%\\.lmstudio\\hub\\models\\%Company%\\%Model%

2nd Windows Location: C:\\Users\\.cache\\%Username%\\.lmstudio\\hub\\models\\%Company%\\%Model%

Linux/Mac Location: ~/.lmstudio/hub/models/%Company%/%Model%
````
%Username% = Name of the user on the PC e.g greg
%Company% = The company that made the model e.g. qwen
%Model% = Name of the model e.g qwen3.5-35b-a3b
````

If the company or model is not there then create the folder and name it appropriately e.g. qwen3.5-35b-a3b. No capitals so that you can use the zip instead without issue in future. Make sure that the file is under the correct company and model.

It is the "base model" folder not a finetune

e.g. 
````
hub\\models\\qwen\\qwen3.5-4b
````
not
````
hub\\models\qwen\\qwen3.5-4b-heretic
or
hub\\models\qwen\\qwen3.5-4b-noromaid-gguf
````

## If you need to add models not included
To add a model not in these: Open the yaml put what is below this under base and fill it out (Go to top of file for ease of locating base):
````
  - key: Insert Publisher/Insert Model  (e.g. AesSedai/Qwen3.5-122B-A10B-GGUF (copy from model page))
    sources:
      - type: huggingface
        user: Insert Publisher (e.g. AesSedai)
        repo: Insert Model (e.g. Qwen3.5-122B-A10B-GGUF)

````

## Thanks 
Yorkie, Roxxus, Lithium, Jedd, and Sol4ra.
