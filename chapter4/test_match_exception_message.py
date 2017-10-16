import pytest


def my_func():
    raise ValueError('Exception 123 raised')


def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        my_func()
