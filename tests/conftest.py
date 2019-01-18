import pytest

from app import create_app

from myproject.extensions import db


@pytest.fixture(scope='module')
def app():
    _app = create_app()

    with _app.app_context():
        db.create_all()

    yield _app

    with _app.app_context():
        db.drop_all()

    return _app


@pytest.fixture
def client(app):
    return app.test_client()
