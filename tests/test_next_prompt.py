from app.services.fake_ai_provider import FakeAIProvider
from app.services.next_service import NextService


def test_next_sends_context_aware_prompt_to_ai():
    ai = FakeAIProvider(
        "ACTION: Ask one potential customer what they would pay.\n"
        "REASON: Real willingness to pay is more useful than guessing.\n"
        "TONE: direct"
    )

    service = NextService(ai_provider=ai)

    service.get_next(
        "I have a business idea but I don't know if people will pay."
    )

    assert ai.last_prompt
    prompt = ai.last_prompt.lower()

    assert "one" in prompt
    assert "action" in prompt
    assert "reason" in prompt
    assert "tone" in prompt
    assert "adapt" in prompt
    assert "actual intent" in prompt
