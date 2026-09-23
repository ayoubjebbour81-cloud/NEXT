from fastapi.testclient import TestClient

from app.main import app


def test_next_api_returns_ai_generated_action():
    with TestClient(app) as client:
        response = client.post(
            "/api/next",
            json={"problem": "I have three business ideas and don't know which one to choose."},
        )

    assert response.status_code == 200

    data = response.json()

    assert data["action"]
    assert data["reason"]
