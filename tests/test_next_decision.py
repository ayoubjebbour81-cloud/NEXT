from app.models.next_decision import NextDecision


def test_next_decision_contains_expected_fields():
    decision = NextDecision(
        action="Ask one customer what they would pay.",
        reason="This gives you real evidence.",
        tone="direct",
        type="experiment",
    )

    assert decision.action == "Ask one customer what they would pay."
    assert decision.reason == "This gives you real evidence."
    assert decision.tone == "direct"
    assert decision.type == "experiment"
