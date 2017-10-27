import pytest

from chapter13.test_skip_imperatively import valid_config


def test_expected_to_fail():
    if not valid_config():
        pytest.xfail('failing configuration (but should work)')
