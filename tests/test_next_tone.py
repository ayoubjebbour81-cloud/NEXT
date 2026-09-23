from app.services.fake_ai_provider import FakeAIProvider
from app.services.next_service import NextService


def test_next_adapts_tone_to_serious_problem():
    ai = FakeAIProvider(
        "ACTION: List all your debts with their balances, interest rates, and due dates.\n"
        "REASON: You need a clear picture of the situation before deciding what to do next.\n"
        "TONE: calm"
    )

    service = NextService(ai_provider=ai)

    result = service.get_next(
        "I am overwhelmed by debt and I don't know where to start."
    )

    assert result.tone == "calm"
    assert result.action
    assert result.reason
    assert "humor" in ai.last_prompt.lower()
    assert "serious" in ai.last_prompt.lower()
