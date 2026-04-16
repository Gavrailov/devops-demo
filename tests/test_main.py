from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_item():
    response = client.get("/items/42?name=test")
    assert response.status_code == 200
    assert response.json()["item_id"] == 42
    assert response.json()["name"] == "test"
