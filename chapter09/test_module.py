import pytest


def setup_function(func):
    print('setting up %s' % func)


def test_func1():
    assert True


@pytest.mark.xfail
def test_func2():
    assert False
