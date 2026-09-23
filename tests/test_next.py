from fastapi.testclient import TestClient

from app.main import app


def test_next_returns_one_action_and_reason():
    with TestClient(app) as client:
        response = client.post(
            "/api/next",
            json={"problem": "I have three business ideas and don't know which one to choose."},
        )

    assert response.status_code == 200

    data = response.json()

    assert "action" in data
    assert "reason" in data
    assert isinstance(data["action"], str)
    assert isinstance(data["reason"], str)
    assert data["action"]
    assert data["reason"]
