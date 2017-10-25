import pytest


@pytest.mark.xfail
def test_ehlo(smtp_param):
    response, msg = smtp_param.ehlo()
    assert response == 250
    assert b'smtp.gmail.com' in msg
    assert 0


@pytest.mark.xfail
def test_noop(smtp_param):
    response, msg = smtp_param.noop()
    assert response == 250
    assert 0
