def pytest_addoption(parser):
    parser.addoption('--string_input', action='append', default=[],
                     help='list of string inputs to pass to test function')


def pytest_generate_tests(metafunc):
    if 'string_input' in metafunc.fixturenames:
        metafunc.parametrize('string_input', metafunc.config.getoption('string_input'))
