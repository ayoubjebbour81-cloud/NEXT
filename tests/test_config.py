from app.core.config import settings


def test_default_settings():
    assert settings.app_name == "NEXT"
    assert settings.app_env == "development"
    assert settings.api_host == "127.0.0.1"
    assert settings.api_port == 8000
