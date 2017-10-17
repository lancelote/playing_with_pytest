import smtplib

import pytest

from chapter4.test_foocompare import Foo


# Custom comparison output
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return ['Comparing Foo instances:', '   values: %s != %s' % (left.val, right.val)]


# Sharing fixture across tests in module
@pytest.fixture(scope='module')  # use 'session' for per-session fixture
def smtp():
    return smtplib.SMTP('smtp.gmail.com', 587, timeout=5)
