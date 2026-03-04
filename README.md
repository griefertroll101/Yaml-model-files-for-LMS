# Issue regarding lmstudio-community/qwen3.5-4B quants 
Unable to fix on my end sadly but you can fix this by moving model folder (i.e. qwen3.5-4b) from the lmstudio-community folder to the unsloth folder and "duplication" be fixed. 

Windows Location: ~C:\\Users\\%Username%\\.lmstudio\\models

2nd Windows Location: ~C:\\Users\\.cache\\%Username%\\.lmstudio\\models

Linux/Mac Location: ~/.lmstudio/models/

I believe it has to do with how the internal code treats lmstudio-community quants and qwen3.5-4b is affected because of something.

# Yaml Model Files For LMS
Note: This is maintained by GrieferTroll in the LM Studio discord. Please do not bother Yags or Yorkie they have better stuff to do. DM me if a issue is here or use the issues tab here.

Plan to add MLX but may be a week or 2 before I do.

Quickly did these up. They contain all//most quants currently available (4th of March 2026) including lmstudio-community but not MLX quants. Unless the model is new then there is little reason these should be updated more than once every 3 or so months but I likely won't update past 3 months.

## Models Done
Qwen 3.5 4B, 9B, 27B, 35B, 122B | OpenAI GPT-OSS 20B, 120B | Z.ai GLM 4.7-flash | Nvidia Nemotron-3-nano

## Install All (Recommended)
Click on the green code at the top of the page and download the zip. Put that zip in the .lmstudio folder and extract all. Open the extracted folder and drag/cut/copy the hub folder into .lmstudio. If prompted Do you want to replace... select yes. 

Windows Location: ~C:\\Users\\%Username%\\.lmstudio

2nd Windows Location: ~C:\\Users\\.cache\\%Username%\\.lmstudio

Linux/Mac Location: ~/.lmstudio

A issue you may run into is that your models may duplicate. If this happens go to C:\Users\%Username%\.lmstudio\models choose the provider (will be in model tab under pblisher) then drag the folder with the name of the duplicated model out of the publisher folder then back in. 

````
%Username% = Name of the user on the PC e.g greg
````

If you do not know the username for the PC then follow the folders one by one i.e start in the Local Disk (C:) then click on the users folder then select the folder that doesn't have the name Default or Public. Once you have selected the %username% folder .lmstudio should be among the folders in that folder.

## Individually

If you want to install model.yaml individually then put under

Windows Location: ~C:\\Users\\%Username%\\.lmstudio\\hub\\models\\%Company%\\%Model%

2nd Windows Location: ~C:\\Users\\.cache\\%Username%\\.lmstudio\\hub\\models\\%Company%\\%Model%

Linux/Mac Location: ~/.lmstudio/hub/models/%Company%/%Model%
````
%Username% = Name of the user on the PC e.g greg
%Company% = The company that made the model e.g. qwen
%Model% = Name of the model e.g qwen3.5-35b-a3b
````

If the company or model is not there then create the folder and name it appropriately

Make sure that the file is under the correct company and model

## If you need to add models not included
To add a model not in these: Open the yaml put what is below this under base and fill it out (Go to top of file for ease of locating base):
````
  - key: Insert Publisher/Insert Model  (e.g. AesSedai/Qwen3.5-122B-A10B-GGUF (copy from model page))
    sources:
      - type: huggingface
        user: Insert Publisher (e.g. AesSedai)
        repo: Insert Model (e.g.wen3.5-122B-A10B-GGUF)

````

## Thanks 
Yorkie, Roxxus, Lithium, Jedd, and Sol4ra
