import pytest


@pytest.fixture(name='parametrized_username')
def fixture_parametrized_username():
    return 'overridden-username'


@pytest.fixture(params=['one', 'two', 'three'], name='non_parametrized_username')
def fixture_non_parametrized_username(request):
    return request.param


def test_username(parametrized_username):
    assert parametrized_username == 'overridden-username'


def test_parametrized_username(non_parametrized_username):
    assert non_parametrized_username in ['one', 'two', 'three']
