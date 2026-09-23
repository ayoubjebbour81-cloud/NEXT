from app.services.fake_ai_provider import FakeAIProvider
from app.services.next_service import NextService


def test_next_identifies_decision_type():
    ai = FakeAIProvider(
        "ACTION: Ask one potential customer what they would pay.\n"
        "REASON: Their answer gives you real evidence before you invest time or money.\n"
        "TONE: direct\n"
        "TYPE: experiment"
    )

    service = NextService(ai_provider=ai)

    result = service.get_next(
        "I have an idea for a service, but I have never asked anyone if they would pay for it."
    )

    assert result.type == "experiment"
    assert "decision" in ai.last_prompt.lower()
    assert "missing information" in ai.last_prompt.lower()
    assert "experiment" in ai.last_prompt.lower()
