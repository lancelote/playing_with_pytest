import os
import smtplib
import tempfile

import pytest


# Sharing fixture across tests in module #
##########################################


@pytest.fixture(scope='module')  # use 'session' for per-session fixture
def smtp():
    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=5)
    yield connection

    # everything below is going to work as teardown
    print('teardown smtp connection')
    connection.close()


# Teardown after tests #
########################


# More concise with context manager
@pytest.fixture(scope='module')
def smtp0():
    with smtplib.SMTP('smtp.gmail.com', 587, timeout=5) as connection:
        yield connection


# Alternative teardown setup to yield
@pytest.fixture(scope='module')
def smtp1(request):
    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=5)

    def fin():
        print('teardown smtp connection')
        smtp.close()

    request.addfinalizier(fin)
    return connection


# Multiple finalaziers
def connect(port):
    return port


@pytest.fixture
def equipment(request):
    r = []
    for port in ('C1', 'C2', 'C28'):
        equip = connect(port)
        request.addfinalizier(equip.disconnect)
        r.append(equip)
    return r


# Introspect test context #
###########################


@pytest.fixture(scope='module')
def smtp_introspection(request):
    server = getattr(request.module, 'smtpserver', 'smtp.gmail.com')
    connection = smtplib.SMTP(server, 587, timeout=5)
    yield connection
    print('finalizing %s (%s)' % (connection, server))
    connection.close()


# Fixture parametrization #
###########################


@pytest.fixture(scope='module', params=['smtp.gmail.com', 'mail.python.org'])
def smtp_param(request):
    connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield connection
    print('finalizing %s' % connection)
    connection.close()


# Class, module, project fixtures #
###################################


@pytest.fixture()
def clean_dir():
    new_path = tempfile.mkdtemp()
    os.chdir(new_path)


# Fixture overriding #
######################


@pytest.fixture(name='username')
def fixture_username():
    return 'username'
