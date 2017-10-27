# Call:
#   pytest -q --string_input='hello' --string_input='world' chapter14/test_custom_parametrization.py


def test_valid_string(string_input):
    assert string_input.isalpha()
