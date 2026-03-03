# Yaml-model-files-for-LMS
Yaml model files for LMS

Plan to add MLX but may be a week or 2 before I do.

Quickly did these up. They contain all/most quants currently available (03/03/2026) including lmstudio-community but not MLX quants. Unless the model is new then there is little reason these should be updated more than once every 3 or so months but I likely won't update past 3 months.

## Models done: 
Qwen 3.5 4B, 9B, 35B, 122B | OpenAI GPT-OSS 20B, 120B | ZAI GLM 4.7-flash, 4.6v-flash | Nvidia Nemotron-3-nano

## Install all (Recommended)
To install all (Recommended) Click on the green code at the top of the page and download the Zip. Put that zip in the .lmstudio folder and extract if prompt if you want to replace the file select yes.

Windows: ~C:\\Users\%Username%\.lmstudio

Linux/Mac: ~/.lmstudio/hub/models/%Company%/%Model%
````
%Username% = Name of the user on the PC e.g greg
%Company% = The company that made the model e.g. qwen
%Model% = Name of the model e.g qwen3.5-35b-a3b
````
## Individually

If you want to install model.yaml individually then put under

Windows: ~C:\\Users\%Username%\.lmstudio\hub\models\\%Company%\\%Model%

Linux/Mac: ~/.lmstudio/hub/models/%Company%/%Model%
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
Yorkie, Roxxus and in part Lithium
