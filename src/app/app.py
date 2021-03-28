import os
import sys
import json
import pprint


TODAYS_MESSAGE = 'hope all is well! Beth and I will placing our order for this month on Saturday. Is there anything you would like us to order for you?'
# TODO: Account for non iMessages (text)
SCRIPT = 'send-message.applescript'

# hope all is well!


def send_messages(data):

    for i in range(len(data['list'])):
        name = data['list'][i]['name']
        number = data['list'][i]['number']
        send = data['list'][i]['send']

        if send == 'Y':

            print('Sending message to {} on number {}'.format(name, number))

            message = 'Hey {}, {}'.format(name, TODAYS_MESSAGE)

            command = 'osascript ../../scripts/{} {} "{}"'.format(
                SCRIPT, number, message)

            os.system(command)


if __name__ == "__main__":

    # Test
    data = {
        "list": [
            {"send": "Y", "name": "Vini", "number": "17607990511"},
            {"send": "Y", "name": "Beth", "number": "17609025715"}
        ]
    }

    send_messages(data)
