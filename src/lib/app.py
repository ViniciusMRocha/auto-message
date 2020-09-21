import os
import sys
import json
import pprint


TODAYS_MESSAGE = 'How is it going for you?'
SCRIPT = 'send-message.applescript'


# with open('src\data\contact-list.json') as file:
#     data = json.load(file)

data = {
    "list": [
        {"name": "Vini", "number": "17607990511"},
        {"name": "Beth", "number": "17609025715"}
    ]
}


for i in range(len(data['list'])):
    name = data['list'][i]['name']
    number = data['list'][i]['number']

    print('Sending message to {} on number {}'.format(name, number))

    message = 'Hey {}, {}'.format(name, TODAYS_MESSAGE)

    command = 'osascript {} {} "{}"'.format(SCRIPT, number, message)

    os.system(command)
