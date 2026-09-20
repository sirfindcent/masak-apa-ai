from fastapi.testclient import TestClient

from api.index import app


client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Masak Apa API is running"
    }


def test_empty_ingredients():
    response = client.post(
        "/api/suggestions",
        json={"ingredients": []},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "At least one ingredient is required."
    }