import warnings

from pytest import deprecated_call


def api_call_v2():
    warnings.warn('use v3 of this api', DeprecationWarning)
    return 200


# noinspection PyDeprecation
def test_deprecated_call():
    with deprecated_call():
        assert api_call_v2() == 200
