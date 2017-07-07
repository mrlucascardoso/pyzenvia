import requests as rq
from .exceptions import ZenviaTokenNotFound, ZenviaUrlNotFound
from decouple import config


class Sender():
    def __init__(self, phone, message, *args, **kwargs):
        self.phone = phone
        self.message = message
        self.settings = load_settings()

    def send(self):
        success = False

        payload = {
            "sendSmsRequest": {
                "from": "Remetente",
                "to": "555199999999",
                "schedule": "2014-08-22T14:55:00",
                "msg": "Mensagem de teste",
                "callbackOption": "NONE",
                "id": "002",
                "aggregateId": "1111"
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'Accept': 'application/json'
        }

        try:
            response = rq.post('url', headers=headers, data=payload)
            if response.ok:
                success = True
        except Exception as err:
            print(err)

        # response_body = urlopen(request).read()
        return success


def load_settings():
    ZENVIA_TOKEN = config('ZENVIA_TOKEN', default=None)
    ZENVIA_URL = config('ZENVIA_URL', default=None)

    if not ZENVIA_TOKEN:
        raise ZenviaTokenNotFound()

    if not ZENVIA_URL:
        raise ZenviaUrlNotFound()

    return {
        'TOKEN': ZENVIA_TOKEN,
        'BASE_URL': ZENVIA_URL
    }
