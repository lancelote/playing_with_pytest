import pytest


@pytest.mark.xfail(raises=IndexError)
def test_list():
    """Check if test fails with specific exception raised."""
    lst = []
    print(lst[1])
