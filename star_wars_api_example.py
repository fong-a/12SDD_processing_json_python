# install requests (pip)
import requests
import json

json_data = requests.get('https://swapi.dev/api/vehicles/')
data = json.loads(json_data.content)

# This particular API limits results to 10 here
for i in data['results']:
    print(i['name'])

