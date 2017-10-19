import pytest


class DB:

    def __init__(self):
        self.in_transaction = []

    def begin(self, name):
        self.in_transaction.append(name)

    def rollback(self):
        self.in_transaction.pop()


@pytest.fixture(scope='module', name='db')
def fixture_db():
    return DB()


class TestClass:

    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self, db):
        assert db.in_transaction == ['test_method1']

    def test_method2(self, db):
        assert db.in_transaction == ['test_method2']
