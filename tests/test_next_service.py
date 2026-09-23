from app.services.next_service import NextService


def test_next_service_returns_one_action_and_reason():
    service = NextService()

    result = service.get_next(
        "I have three business ideas and don't know which one to choose."
    )

    assert result.action
    assert result.reason
