import pytest


@pytest.fixture(name='smtp')
def fixture_smtp():
    import smtplib
    return smtplib.SMTP('smtp.gmail.com', 587, timeout=5)


def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
