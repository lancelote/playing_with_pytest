from pytest import approx, raises


def test_simple_sum():
    assert 0.1 + 0.2 == approx(0.3)


def test_sequence():
    assert (0.1 + 0.2, 0.2 + 0.4) == approx((0.3, 0.6))


def test_dictionary_values():
    assert {'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == approx({'a': 0.3, 'b': 0.6})


def test_changing_tolerance():
    assert not 1.0001 == approx(1)
    assert 1.0001 == approx(1, rel=1e-3)
    assert 1.0001 == approx(1, abs=1e-3)
    assert 1 + 1e-8 == approx(1)
    assert not 1 + 1e-8 == approx(1, abs=1e-12)
    assert 1 + 1e-8 == approx(1, rel=1e-6, abs=1e-12)


def test_unsupported_comparison_operators():
    with raises(TypeError):
        assert approx(0.1) > 0.1 + 1e-10
    with raises(TypeError):
        assert 0.1 + 1e-10 > approx(0.1)
