import pytest
from pyzenvia.sender import send_sms

def test_send_sms():
    data = send_sms()
    assert type(data) == str
