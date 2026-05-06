import json
# python object to json string+file 
# this is a way to create a file and store information ! inside bornil.json file



bornil = {
  "name": "bornil mahmud ",
  "age " : 22,
  "city" : "khoksa",
  "status" : False, 
  "play" : ["football","cricket","badmintion"]
}

with open ("bornil.json" ,"w")as jsonfile:
  json.dump(bornil,jsonfile,indent=4)
  