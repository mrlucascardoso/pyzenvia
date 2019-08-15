from pyzenvia.sender import Sender


def test_send_one_sms():
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
