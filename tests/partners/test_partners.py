from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK
from app.main import app


client = TestClient(app)


def test_create_partner():
    json_partner = {"name": "partner"}
    response = client.post("/partners", json=json_partner)

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"partner": json_partner}
