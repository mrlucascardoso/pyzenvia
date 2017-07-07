import requests as rq
from .exceptions import ZenviaTokenNotFound, ZenviaUrlNotFound, InvalidArgument
from decouple import config


class Sender():
    def __init__(self, phones, message, *args, **kwargs):

        if not phones:
            raise InvalidArgument('The argument phones must be a string of numbers or list of strings of numbers.')

        if type(phones) == str:
            self.phones = [phones, ]
        elif type(phones) == list:
            if not all(type(phone) is str for phone in phones):
                raise InvalidArgument('The items in list phones must be a string.')

            phones = [phone.strip() for phone in phones]

            if not all(phone != '' for phone in phones):
                raise InvalidArgument('The items in list phones must be a not cleaned string.')
            self.phones = phones

        # Check for message is not None or cleaned string or not string
        if not message or type(message) != str:
            raise InvalidArgument('The argument message must be a string.')

        # Check for length string
        if len(message) > 160:
            raise InvalidArgument('Message size must be less than or equal to 160 characters.')

        self.message = message
        self.settings = load_settings()
        for key, value in kwargs.items():
            setattr(self, key, value)


    def _send(self, phone, message):
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

    def send(self):
        success = False

        data = [self._send(phone, self.message) for phone in self.phones]

        success = all(_['success'] for _ in data)
        results = [_['result'] for _ in data]

        return {'success': success, 'results': results}




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
