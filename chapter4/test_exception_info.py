import pytest


def test_recursion_depth():
    """Exception parameters."""
    with pytest.raises(RuntimeError) as exc_info:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(exc_info)
