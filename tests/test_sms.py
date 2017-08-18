from pyzenvia.sender import Sender


def test_send_one_sms():
    sender = Sender('eng', '123')
    data = sender.send('5586999181896','Test')
    assert data                                                     # Check for data is generated
    assert type(data) == dict                                       # Check for data type is dict
    assert 'success' in data                                        # Check for 'success' key is in returned data
    assert 'result' in data                                        # Check for 'results' key is in returned data
    assert data['success'] == True                                  # Check for message was sended


def test_send_multiple_sms():
    pass


def test_send_schedule_sms():
    pass
