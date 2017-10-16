import pytest


def test_custom_raises_message():
    with pytest.raises(ZeroDivisionError, message='expecting ZeroDivisionError'):
        print(1 / 0)
