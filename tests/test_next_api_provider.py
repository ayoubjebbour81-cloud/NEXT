from app.services.fake_ai_provider import FakeAIProvider
from app.services.next_service import NextService


def test_next_service_can_be_used_by_api_with_fake_ai():
    ai = FakeAIProvider(
        response="ACTION: Call the first potential customer today."
    )

    service = NextService(ai_provider=ai)

    result = service.get_next(
        "I don't know how to validate my business idea."
    )

    assert result.action == "Call the first potential customer today."
