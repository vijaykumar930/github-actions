import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    """Test that the hello route returns 'Hello, World!' in JSON format"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, World!'}


def test_hello_route_content_type(client):
    """Test that the hello route returns application/json content type"""
    response = client.get('/')
    assert response.content_type == 'application/json'
