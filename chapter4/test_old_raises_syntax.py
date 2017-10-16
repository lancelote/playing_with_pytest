import pytest


def test_compatibility_with_old_python_2():
    """Syntax for Python 2.4."""
    def f(param1, param2):
        return param1 / param2

    pytest.raises(ZeroDivisionError, f, 1, param2=0)
    pytest.raises(ZeroDivisionError, 'f(1, param2=0)')
