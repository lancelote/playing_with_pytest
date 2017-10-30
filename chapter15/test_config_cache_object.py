import time

import pytest


@pytest.fixture(name='my_data')
def fixture_my_data(request):
    val = request.config.cache.get('example/value', None)
    if val is None:
        time.sleep(9 * 0.6)  # expensive computation
        val = 42
        request.config.cache.set('example/value', val)
    return val


def test_function(my_data):
    """Call twice and check time difference.

    To see cache, call:
        pytest --cache-show

    To clear cache:
        pytest --cache-clear
    """
    return my_data == 42
