from types import SimpleNamespace

from app.services.openai_provider import OpenAIProvider


class FakeResponses:
    def create(self, **kwargs):
        assert kwargs["model"] == "gpt-5"
        assert kwargs["input"] == "Give me one next action."

        return SimpleNamespace(
            output_text="Ask one potential customer today."
        )


class FakeClient:
    def __init__(self):
        self.responses = FakeResponses()


def test_openai_provider_generates_text():
    provider = OpenAIProvider(
        api_key="test-key",
        model="gpt-5",
    )

    provider.client = FakeClient()

    result = provider.generate("Give me one next action.")

    assert result == "Ask one potential customer today."
