import json
# python object to json string


bornil = {
  "name": "bornil mahmud ",
  "age " : 22,
  "city" : "khoksa",
  "status" : False, 
  "play" : ["football","cricket","badmintion"]
}

result = json.dumps(bornil,indent=4)
print(result)