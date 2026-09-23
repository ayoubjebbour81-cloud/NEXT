from app.models.next_decision import NextDecision
from app.services.fake_ai_provider import FakeAIProvider
from app.services.next_service import NextService


def test_next_service_returns_next_decision():
    ai = FakeAIProvider(
        "ACTION: Ask one customer what they would pay.\n"
        "REASON: This gives you real evidence.\n"
        "TONE: direct\n"
        "TYPE: experiment"
    )

    service = NextService(ai_provider=ai)

    result = service.get_next(
        "I have a business idea but I don't know if people will pay."
    )

    assert isinstance(result, NextDecision)
    assert result.action == "Ask one customer what they would pay."
    assert result.reason == "This gives you real evidence."
    assert result.tone == "direct"
    assert result.type == "experiment"
