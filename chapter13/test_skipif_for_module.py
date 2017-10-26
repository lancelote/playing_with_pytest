import sys

import pytest

pytestmark = pytest.mark.skipif(sys.platform == 'darwin', reason='skip on macOS')


def test_will_be_skipped_1():
    pass


def test_will_be_skipped_2():
    pass
