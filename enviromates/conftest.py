import pytest
from enviromates import app





@pytest.fixture
def api():
    client = app.test_client()
    return client
    
@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
