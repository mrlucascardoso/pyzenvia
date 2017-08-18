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

    def send(self, phone, message, **kwargs):
        result = {}
        success = False
        if self.api == APIVersion.V1:
            url = '{url}&account={account}&code={password}&to={phone}&msg={message}'.format(
                url=self.get_url('send'),
                account=self.account,
                password=self.password,
                phone=phone,
                message=message
            )

            for key in kwargs.keys():
                url += '&{key}={value}'.format(key=key, value=kwargs[key])

            try:
                response = rq.get(url, headers=self.get_headers())
                result = response.text
                if response.ok:
                    success = True
            except Exception as err:
                print(err)

            return {'success': success, 'result': result}
        else:
            raise NotImplementedError()
