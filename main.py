import requests
import json

print('How many humans are in space right now?')
resp = requests.get('http://api.open-notify.org/astros.json')

json_resp = json.loads(resp.text)

print('Currently there are ' + str(json_resp['number']) + ' in space.')
print('They are :-')
for person in json_resp['people']:
    print(person['name'], ' in ', person['craft'])
