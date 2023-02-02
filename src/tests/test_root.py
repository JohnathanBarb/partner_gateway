from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK
from src.app import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "Welcome to Partner Gateway"}
