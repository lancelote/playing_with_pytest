import pytest


def f():
    raise SystemExit


def test_my_test():
    with pytest.raises(SystemExit):
        f()
