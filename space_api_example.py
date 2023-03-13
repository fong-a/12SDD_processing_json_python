# install requests (pip)
import requests
import json

# this website is driven by the following open api https://whoisinspace.com/ß

json_data = requests.get('http://api.open-notify.org/astros.json')
data = json.loads(json_data.content)

print(data['number'])
# This particular API limits results to 10 here
for i in data['people']:
    print(i)



