import sys

import pytest


@pytest.mark.xfail(sys.version_info >= (3, 3), reason='Python 3.3 API changes')
def test_fail_with_reason():
    assert False
