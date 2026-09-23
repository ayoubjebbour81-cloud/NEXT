from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_next_api_returns_type():
    response = client.post(
        "/api/next",
        json={"problem": "I have two options and need to decide which one to choose."},
    )

    assert response.status_code == 200
    data = response.json()

    assert "action" in data
    assert "reason" in data
    assert "tone" in data
    assert "type" in data
