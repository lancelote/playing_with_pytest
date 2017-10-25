import pytest

smtpserver = 'mail.python.org'


@pytest.mark.xfail
def test_show_helo(smtp_introspection):
    assert 0, smtp_introspection.helo()
