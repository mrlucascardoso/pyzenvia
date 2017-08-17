import requests as rq

from pyzenvia.config import URLS
from pyzenvia.enums import APIVersion
import base64


class Sender():
    def __init__(self, account, password, debug=False, api=APIVersion.V1, *args, **kwargs):
        self.account = account
        self.password = password
        self.api = api
        self.debug = debug
        self.args = args
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_url(self, operation):
        return URLS[self.api]['debug'][operation] if self.debug else URLS[self.api]['production'][operation]

    def get_token(self):
        token = '{}:{}'.format(self.account, self.password)
        return base64.b64encode(bytes(token, 'utf-8')).decode('utf-8')

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic {}'.format(self.get_token())
        }

    def send(self, phone, message):
        result = {}
        success = False

        url = self.settings['BASE_URL'] + '/services/send-sms'

        dispatcher = getattr(self, 'dispatcher', '')
        schedule = getattr(self, 'schedule', '')
        callback_option = getattr(self, 'callback_option', 'NONE')
        _id = getattr(self, 'id', '')
        aggregate_id = getattr(self, 'aggregate_id', '')

        payload = {
            "sendSmsRequest": {
                "from": dispatcher,
                "to": phone,
                "schedule": schedule,
                "msg": message,
                "callbackOption": callback_option,
                "id": _id,
                "aggregateId": aggregate_id
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + self.settings['TOKEN'],
            'Accept': 'application/json'
        }

        try:
            response = rq.post(url, headers=headers, data=payload)
            if response.ok:
                success = True
                result = response.json()

        except Exception as err:
            print(err)

        return {'success': success, 'result': result}
