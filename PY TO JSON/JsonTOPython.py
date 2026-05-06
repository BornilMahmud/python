import json

bornil = """
{
  "name": "bornil mahmud",
  "age": 22,
  "city": "khoksa",
  "status": false,
  "play": ["football", "cricket", "badminton"]
}
"""

result = json.loads(bornil)

print(result)