from fastapi.testclient import TestClient

from app.main import create_app
from app.services.fake_ai_provider import FakeAIProvider


def test_next_api_uses_injected_ai_provider():
    ai = FakeAIProvider(
        "ACTION: Ask one customer to describe the problem.\n"
        "REASON: Their answer gives you real evidence.\n"
        "TONE: direct\n"
        "TYPE: experiment"
    )

    test_app = create_app(ai_provider=ai)

    with TestClient(test_app) as client:
        response = client.post(
            "/api/next",
            json={"problem": "I have an idea but I have not tested it."},
        )

    assert response.status_code == 200
    data = response.json()

    assert data["action"] == "Ask one customer to describe the problem."
    assert data["reason"] == "Their answer gives you real evidence."
    assert data["tone"] == "direct"
    assert data["type"] == "experiment"
