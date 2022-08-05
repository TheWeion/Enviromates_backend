import pytest
from .routes.users import users_routes


@pytest.fixture
def api():
    client = users_routes.users.test_client()
    return client