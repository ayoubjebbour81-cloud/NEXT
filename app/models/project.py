from datetime import datetime
from uuid import UUID, uuid4


class Project:
    def __init__(
        self,
        name: str,
        goal: str,
        deadline: datetime,
        achieved_at: datetime | None = None,
    ):
        self.id: UUID = uuid4()
        self.name = name
        self.goal = goal
        self.deadline = deadline
        self.achieved_at = achieved_at

    def mark_achieved(self, achieved_at: datetime) -> None:
        self.achieved_at = achieved_at

    @property
    def achieved_on_time(self) -> bool:
        if self.achieved_at is None:
            return False

        return self.achieved_at <= self.deadline
