from chapter04.test_foocompare import Foo


# Custom comparison output #
############################


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return ['Comparing Foo instances:', '   values: %s != %s' % (left.val, right.val)]
