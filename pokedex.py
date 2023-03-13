import json

f = open('pokedex.json')
  
# returns JSON object as a dictionary
f = json.load(f)

print(f)


