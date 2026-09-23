from app.services.fake_ai_provider import FakeAIProvider
from app.services.next_service import NextService


def test_next_service_uses_ai_provider():
    ai = FakeAIProvider(
        response="ACTION: Ask the three founders for their available budget."
    )

    service = NextService(ai_provider=ai)

    result = service.get_next(
        "I have three business ideas and don't know which one to choose."
    )

    assert result.action == "Ask the three founders for their available budget."


def test_next_service_parses_decision_type():
    ai = FakeAIProvider(
        response=(
            "ACTION: Ask one customer what they would pay.\n"
            "REASON: Real willingness to pay is better than guessing.\n"
            "TONE: direct\n"
            "TYPE: experiment"
        )
    )

    service = NextService(ai_provider=ai)

    result = service.get_next(
        "I have a business idea but I don't know if people will pay."
    )

    assert result.type == "experiment"
