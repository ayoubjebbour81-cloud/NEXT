from app.services.openai_provider import OpenAIProvider


def test_openai_provider_uses_app_settings():
    provider = OpenAIProvider(
        api_key="test-key",
        model="gpt-5",
    )

    assert provider.model == "gpt-5"
