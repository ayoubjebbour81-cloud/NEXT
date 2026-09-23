from app.services.openai_provider import OpenAIProvider


def test_openai_provider_can_be_created():
    provider = OpenAIProvider(
        api_key="test-key",
        model="gpt-5",
    )

    assert provider.model == "gpt-5"
