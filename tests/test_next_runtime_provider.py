from fastapi.testclient import TestClient

from app.main import app
from app.services.next_service import NextService
from app.services.openai_provider import OpenAIProvider


def test_app_uses_openai_provider():
    with TestClient(app) as client:
        service = app.state.next_service

        assert isinstance(service, NextService)
        assert isinstance(service.ai_provider, OpenAIProvider)
