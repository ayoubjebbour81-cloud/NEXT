from app.services.fake_ai_provider import FakeAIProvider
from app.services.next_service import NextService


def test_next_returns_action_reason_and_tone():
    ai = FakeAIProvider(
        "ACTION: Ask three potential customers what they would pay.\n"
        "REASON: Their willingness to pay matters more than your assumptions.\n"
        "TONE: direct"
    )

    service = NextService(ai_provider=ai)

    result = service.get_next(
        "I have a business idea but I don't know if people will pay for it."
    )

    assert result.action == "Ask three potential customers what they would pay."
    assert result.reason == "Their willingness to pay matters more than your assumptions."
    assert result.tone == "direct"
