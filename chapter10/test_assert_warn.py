import warnings

import pytest


def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn('my warning', UserWarning)


def raise_warning():
    warnings.warn('my warning', UserWarning)


def test_old_style():
    pytest.warns(UserWarning, raise_warning)
    pytest.warns(UserWarning, 'raise_warning()')


def test_warnings_list():
    with pytest.warns(RuntimeWarning) as record:
        warnings.warn('another warning', RuntimeWarning)

    assert len(record) == 1
    assert record[0].message.args[0] == 'another warning'
