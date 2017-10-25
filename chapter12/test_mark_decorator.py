import pytest

mark1 = pytest.mark.NAME  # simple MarkDecorator
mark2 = pytest.mark.NAME(name1='value')  # parametrized MarkDecorator


@mark2
def test_function():
    pass
