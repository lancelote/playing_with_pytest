"""
run `pytest --collect-only`

...
<Module 'test_ids.py'>
  <Function 'test_a[spam]'>
  <Function 'test_a[ham]'>
  <Function 'test_b[eggs]'>
  <Function 'test_b[1]'>
...
"""

import pytest


@pytest.fixture(params=[0, 1], ids=['spam', 'ham'], name='a')
def fixture_a(request):
    return request.param


def test_a(a):
    assert a > -1


def idfn(fixture_value):
    if fixture_value == 0:
        return 'eggs'
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn, name='b')
def fixture_b(request):
    return request.param


def test_b(b):
    assert b > -1
