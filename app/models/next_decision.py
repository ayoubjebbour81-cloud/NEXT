from dataclasses import dataclass


@dataclass(frozen=True)
class NextDecision:
    action: str
    reason: str
    tone: str
    type: str
