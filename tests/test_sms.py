from pyzenvia.sender import Sender
from pyzenvia.sender import load_settings


def test_load_settings():
    settings = load_settings()
    assert settings
    assert type(settings) == dict


def test_send_sms():
    sender = Sender('+5586999776633', 'Mensagem de teste')
    data = sender.send()
    assert type(data) == bool
    assert data
