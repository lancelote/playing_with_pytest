import pytest

from chapter13 import my_module

min_version = pytest.mark.skipif(my_module.__version__ < (1, 1), reason='my_module >= v1.1 required')


@min_version
def test_another_function():
    pass
