import pytest


@pytest.fixture(name='username')
def fixture_username(username):
    return 'overridden-else-' + username


def test_username(username):
    assert username == 'overridden-else-username'
