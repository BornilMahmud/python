import json
# we will need the bornil.json file inside the vscode ! 

with open("bornil.json","r") as pythonfile:
    pythonobj=json.load(pythonfile)
    #then convert this into json string 
    pythonJson=json.dumps(pythonobj,indent =4)
    print(pythonJson)
    
    