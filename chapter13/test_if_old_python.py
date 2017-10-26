import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 3), reason='requires Python 3.3')
def test_function():
    pass
