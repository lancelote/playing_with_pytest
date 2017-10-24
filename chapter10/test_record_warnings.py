import warnings

import pytest


def test_record_with_pytest_warn():
    with pytest.warns(None) as record:
        warnings.warn('user', UserWarning)
        warnings.warn('runtime', RuntimeWarning)

    assert len(record) == 2
    assert str(record[0].message) == 'user'
    assert str(record[1].message) == 'runtime'


def test_record_with_recwarn(recwarn):
    warnings.warn('hello', UserWarning)
    assert len(recwarn) == 1
    warning = recwarn.pop(UserWarning)
    assert issubclass(warning.category, UserWarning)
    assert str(warning.message) == 'hello'
    assert warning.filename
    assert warning.lineno
