from app.services.ai_provider import AIProvider


def test_ai_provider_defines_generate():
    assert hasattr(AIProvider, "generate")
