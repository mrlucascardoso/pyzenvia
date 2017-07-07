from pyzenvia.sender import Sender
from pyzenvia.sender import load_settings


def test_load_settings():
    settings = load_settings()
    assert settings
    assert type(settings) == dict


def test_send_one_sms():
    sender = Sender(['5586912345678'], 'Testando')
    data = sender.send()
    assert data                                                     # Check for data is generated
    assert type(data) == dict                                       # Check for data type is dict
    assert 'success' in data                                        # Check for 'success' key is in returned data
    assert 'results' in data                                        # Check for 'results' key is in returned data
    assert data['success'] == True                                  # Check for message was sended
    assert type(data['results']) == list                            # Check for 'results' type is a list
    assert len(data['results']) > 0                                 # Check for 'results' has gran than one
    assert all(type(_) is dict for _ in data['results'])            # Check for each item in 'results' is a dict
    assert all(_ != {} for _ in data['results'])                    # Check for each item in 'results' is not cleaned dict


def test_send_multiple_sms():
    pass


def test_send_schedule_sms():
    pass
