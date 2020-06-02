import argparse

from pyzenvia.sender import Sender
from pyzenvia.enums import APIVersion

parser = argparse.ArgumentParser(description='Send SMS using Zenvia gateway')
parser.add_argument('--account', help='Zenvia account id')
parser.add_argument('--password', help='Zenvia account password')
parser.add_argument('phone', help='Recipient phone number (eg: 55xxyyyyykkkk')
parser.add_argument('message', help='SMS message')

args = parser.parse_args()

sms = Sender(args.account, args.password, api=APIVersion.V2)
response = sms.send(args.phone, args.message)

if response['success'] == True:
    print(f'SMS sent to {args.phone}')
else:
    print(f'Error sending SMS to {args.phone}')
