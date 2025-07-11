import pytest
from app.hello_world import app

def test_hello_world():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data.decode() == "Hello World!"
