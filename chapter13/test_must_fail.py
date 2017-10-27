import pytest


@pytest.mark.xfail(strict=True)
def test_must_fail_func():
    assert False
