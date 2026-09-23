from fastapi.testclient import TestClient

from app.main import app


def test_root_serves_next_ui():
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<title>NEXT</title>" in response.text
    assert 'id="next-button"' in response.text
