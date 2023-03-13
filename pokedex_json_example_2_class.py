import json

# create a class definition

class Pokemon:
    def __init__(self, id, name):
        self.id = id
        self.name = name

pokemon = []

# open the json file, create dictionary, then instantiate objects based on class above

with open('pokedex.json') as json_data:
    data = json.loads(json_data.read())
    for i in data:
        new_pokemon = Pokemon(i['id'],i['name']['english'])
        pokemon.append(new_pokemon)

for i in pokemon:
    print(i.name)

# for i in pokemon:
#     if len(i.name) > 5:
#         print(i.name)
    

 