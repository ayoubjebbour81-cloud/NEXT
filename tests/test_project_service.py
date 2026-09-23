from datetime import datetime, timedelta

from app.models.project import Project
from app.services.project_service import ProjectService


def test_project_service_returns_project():
    service = ProjectService()
    deadline = datetime.now() + timedelta(days=30)

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
    )

    result = service.get_project(project)

    assert result is project
