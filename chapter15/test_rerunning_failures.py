"""
pytest --lf chapter15/test_rerunning_failures.py  # run only last failures
pytest --ff chapter15/test_rerunning_failures.py  # run failures first
"""

import pytest


@pytest.mark.xfail  # comment this out
@pytest.mark.parametrize('i', range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail('bad luck')
