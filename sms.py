import os
from twilio.rest import Client

account_sid = os.environ['SID']
auth_token = os.environ['TOKEN']
client = Client(account_sid, auth_token)

sender = os.environ['FROM']
recipient = os.environ['TO']


def send_sms(obj):
    body = '\nCurrently there are ' + str(obj['number']) + ' in space.\n'
    body = body + 'They are :- \n'
    for person in obj['people']:
        body = body + person['name'] + ' in ' + person['craft'] + '\n'

    print(body)
    message = client.messages.create(
        body=body,
        from_=sender,
        to=recipient
    )

    print(message.sid)
    print('SMS sent to ', recipient)
