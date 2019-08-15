import requests

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
        url = URLS[self.api]['production'][operation]

        if self.debug:
            url = URLS[self.api]['debug'][operation]

        return url

    @property
    def get_token(self):
        token = '{}:{}'.format(self.account, self.password)
        return base64.b64encode(bytes(token, 'utf-8')).decode('utf-8')

    @property
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Basic {self.get_token}'
        }

    def send(self, phone, message, **kwargs):
        result = {}
        success = False
        if self.api == APIVersion.V1:
            url = f'{self.get_url("send")}\
                &account={self.account}\
                &code={self.password}\
                &to={phone}\
                &msg={message}'

            for key in kwargs.keys():
                url += f'&{key}={kwargs[key]}'

            try:
                response = requests.get(url, headers=self.get_headers)
                result = response.text
                if response.ok:
                    success = True
            except Exception as err:
                return {
                    'success': success,
                    'result': None,
                    'error': {
                        'message': str(err),
                        'exception': err
                    }
                }

            return {
                'success': success,
                'result': result,
                'error': None
            }
        else:
            raise NotImplementedError()
