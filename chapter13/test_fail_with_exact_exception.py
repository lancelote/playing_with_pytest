import pytest


@pytest.mark.xfail(raises=RuntimeError)
def test_fail_with_runtime_error():
    raise RuntimeError
