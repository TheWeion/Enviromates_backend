import pytest
from enviromates import app
from flask import blueprints


@pytest.fixture
def api():
    client = app.test_client()
    return client