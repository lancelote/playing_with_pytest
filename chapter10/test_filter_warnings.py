import warnings

import pytest


# to turn all warnings into error
# pytestmark = pytest.mark.filterwarnings('error')


def api_v1():
    warnings.warn(UserWarning('api v1, should use functions from v2'))
    return 1


@pytest.mark.filterwarnings('ignore:api v1')
def test_one():
    assert api_v1() == 1
