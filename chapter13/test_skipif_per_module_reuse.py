from chapter13.test_skipif_per_module import min_version


@min_version
def test_another_function():
    pass
