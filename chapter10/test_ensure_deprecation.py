import warnings

import pytest


def api_call_v2():
    warnings.warn('use v3 of this api', DeprecationWarning)


# noinspection PyDeprecation
def test_deprecated():
    pytest.deprecated_call(api_call_v2())


def test_deprecated_with_recwarn(recwarn):
    warnings.simplefilter('always')
    warnings.warn('deprecated', DeprecationWarning)
    assert len(recwarn) == 1
    assert recwarn.pop(DeprecationWarning)


# noinspection PyDeprecation
def test_deprecated_with_context():
    with pytest.deprecated_call():
        api_call_v2()
