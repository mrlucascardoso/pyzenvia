from pyzenvia.sender import Sender
from pyzenvia.enums import APIVersion


def test_send_one_sms_api_v1():
    sender = Sender('eng', '123')
    data = sender.send('5586999181896', 'Test')
    # Check for data is generated
    assert data
    # Check for data type is dict
    assert type(data) == dict
    # Check for 'success' key is in returned data
    assert 'success' in data
    # Check for 'results' key is in returned data
    assert 'result' in data
    # Check for message was sended
    assert data['success'] == True


def test_send_multiple_sms():
    pass


def test_send_schedule_sms():
    pass


def test_send_one_sms_api_v2():
    sms = Sender('account', 'password', api=APIVersion.V2)
    data = sms.send('55xxxxxxxxxxx', 'Hello from pyzenvia', sender="Remetente")

    # Check for data is generated
    assert data
    # Check for data type is dict
    assert type(data) == dict
    # Check for 'success' key is in returned data
    assert 'success' in data
    # Check for 'results' key is in returned data
    assert 'result' in data
    # Check for message was sended
    assert data['success'] == True
