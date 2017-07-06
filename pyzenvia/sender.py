import requests

class Sender():
  def __init__(self, phone, message, *args, **kwargs):
    self.phone = phone
    self.message = message


  def send(self):
      # values = """
      #   {
      #     "sendSmsRequest": {
      #       "from": "Remetente",
      #       "to": "555199999999",
      #       "schedule": "2014-08-22T14:55:00",
      #       "msg": "Mensagem de teste",
      #       "callbackOption": "NONE",
      #       "id": "002",
      #       "aggregateId": "1111"
      #     }
      #   }
      # """

      # headers = {
      #   'Content-Type': 'application/json',
      #   'Authorization': 'Basic YWRtaW46YWRtaW4=',
      #   'Accept': 'application/json'
      # }
      # request = Request('https://private-anon-31f1cb2966-zenviasms.apiary-mock.com/services/send-sms', data=values, headers=headers)

      # response_body = urlopen(request).read()
      return True
