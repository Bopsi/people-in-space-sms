# people-in-space-sms
Python program to get the number of people in space right now and sends this information as SMS

##API
http://api.open-notify.org/astros.json

##Sms Client
https://www.twilio.com/

##Configuration
Add a `.env` file in project root and add following information
```dotenv
#Twilio API keys
SID="twilio SID"
TOKEN="twilio token"

#Twilio contacts
FROM="twilio trial account number"
TO="twilio verified number"
```

##Run
```sh
pipenv run python main.py
```