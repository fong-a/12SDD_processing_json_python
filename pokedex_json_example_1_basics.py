import json

# To work with JSON in Python, you need to import the json module first, 
# then call json.loads() method to parse the JSON string to a Python object.

# Opening JSON file
f = open('pokedex.json')
  
# returns JSON object as a dictionary
data = json.load(f)
  
# loop through the json dictionary items
for i in data:
    if len(i['name']['english'])>11:
        print(i['name']['english'])

# for i in data:
#     if i['base']['HP'] > 100 :
#         print(i['name']['english'])

# Close the file 
f.close()

# Task A - Search by "Grass Type"

# Task B - Attack must be over 50

# Task C - HP over 200