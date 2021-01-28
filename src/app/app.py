import os
import sys
import json
import pprint


TODAYS_MESSAGE = 'Beth and I will be placing an order in the next couple of days. Is there anything you would like?'
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

    # Real data
    with open('../data/contact-list.json', 'r') as file:
        data = json.load(file)
        pprint.pprint(data)

    # # Test
    # data = {
    #     "list": [
    #         {"send": "Y", "name": "Vini", "number": "17607990511"},
    #         {"send": "N", "name": "Beth", "number": "17609025715"}
    #     ]
    # }

    send_messages(data)
