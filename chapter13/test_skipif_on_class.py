import sys

import pytest


@pytest.mark.skipif(sys.platform == 'win32', reason='does not run on windows')
class TestPosixCalls:
    def test_function(self):
        """Will not be setup or run on Windows."""
        pass
