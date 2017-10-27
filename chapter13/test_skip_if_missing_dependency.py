import pytest

docutils = pytest.importorskip('docutils')


# Specify minor version
# docutils = pytest.importorskip('docutils', minversion='0.3')


@docutils
def test_skit_if_no_docutils():
    pass
