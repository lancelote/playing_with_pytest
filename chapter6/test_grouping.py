"""
pytest -v -s test_grouping.py

chapter6/test_grouping.py::test_0[1]   SETUP other_args 1
  RUN test0 with other_arg 1
PASSED  TEARDOWN other_arg 1

chapter6/test_grouping.py::test_0[2]   SETUP other_args 2
  RUN test0 with other_arg 2
PASSED  TEARDOWN other_arg 2

chapter6/test_grouping.py::test_1[mod1]   SETUP mod_arg mod1
  RUN test1 with mod_arg mod1
PASSED
chapter6/test_grouping.py::test_2[1-mod1]   SETUP other_args 1
  RUN test2 with other_arg 1 and mod_arg mod1
PASSED  TEARDOWN other_arg 1

chapter6/test_grouping.py::test_2[2-mod1]   SETUP other_args 2
  RUN test2 with other_arg 2 and mod_arg mod1
PASSED  TEARDOWN other_arg 2

chapter6/test_grouping.py::test_1[mod2]   TEARDOWN mod_arg mod1
  SETUP mod_arg mod2
  RUN test1 with mod_arg mod2
PASSED
chapter6/test_grouping.py::test_2[1-mod2]   SETUP other_args 1
  RUN test2 with other_arg 1 and mod_arg mod2
PASSED  TEARDOWN other_arg 1

chapter6/test_grouping.py::test_2[2-mod2]   SETUP other_args 2
  RUN test2 with other_arg 2 and mod_arg mod2
PASSED  TEARDOWN other_arg 2
  TEARDOWN mod_arg mod2
"""

import pytest


@pytest.fixture(scope='module', params=['mod1', 'mod2'], name='mod_arg')
def fixture_mod_arg(request):
    param = request.param
    print('  SETUP mod_arg %s' % param)
    yield param
    print('  TEARDOWN mod_arg %s' % param)


@pytest.fixture(scope='function', params=[1, 2], name='other_arg')
def fixture_other_arg(request):
    param = request.param
    print('  SETUP other_args %s' % param)
    yield param
    print('  TEARDOWN other_arg %s' % param)


def test_0(other_arg):
    print('  RUN test0 with other_arg %s' % other_arg)


def test_1(mod_arg):
    print('  RUN test1 with mod_arg %s' % mod_arg)


def test_2(other_arg, mod_arg):
    print('  RUN test2 with other_arg %s and mod_arg %s' % (other_arg, mod_arg))
