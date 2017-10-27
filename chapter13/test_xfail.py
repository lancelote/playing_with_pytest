import pytest


@pytest.mark.xfail
def test_expected_to_fail():
    assert False
