import requests
import json
from sms import send_sms

print('How many humans are in space right now?')
resp = requests.get('http://api.open-notify.org/astros.json')

json_resp = json.loads(resp.text)

send_sms(json_resp)
