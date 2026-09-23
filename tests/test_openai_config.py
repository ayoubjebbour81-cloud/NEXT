from app.core.config import settings


def test_openai_settings_exist():
    assert hasattr(settings, "openai_api_key")
    assert hasattr(settings, "openai_model")
    assert settings.openai_model
