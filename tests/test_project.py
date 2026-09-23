from datetime import datetime, timedelta

from app.models.project import Project


def test_project_records_goal_achieved_at():
    deadline = datetime.now() + timedelta(days=30)
    achieved_at = datetime.now()

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
        achieved_at=achieved_at,
    )

    assert project.achieved_at == achieved_at


def test_project_knows_if_goal_was_achieved_on_time():
    deadline = datetime.now() + timedelta(days=30)
    achieved_at = datetime.now()

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
        achieved_at=achieved_at,
    )

    assert project.achieved_on_time is True


def test_project_knows_if_goal_was_achieved_late():
    deadline = datetime.now()
    achieved_at = deadline + timedelta(minutes=1)

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
        achieved_at=achieved_at,
    )

    assert project.achieved_on_time is False


def test_project_knows_when_goal_is_not_achieved_yet():
    deadline = datetime.now() + timedelta(days=30)

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
    )

    assert project.achieved_at is None
    assert project.achieved_on_time is False


def test_project_considers_exact_deadline_on_time():
    deadline = datetime.now()

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
        achieved_at=deadline,
    )

    assert project.achieved_on_time is True


def test_project_has_id():
    deadline = datetime.now() + timedelta(days=30)

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
    )

    assert project.id is not None


def test_projects_have_unique_ids():
    deadline = datetime.now() + timedelta(days=30)

    project_one = Project(
        name="Project One",
        goal="Goal One",
        deadline=deadline,
    )

    project_two = Project(
        name="Project Two",
        goal="Goal Two",
        deadline=deadline,
    )

    assert project_one.id != project_two.id


def test_project_can_be_marked_as_achieved():
    deadline = datetime.now() + timedelta(days=30)

    project = Project(
        name="My Project",
        goal="Build a profitable business",
        deadline=deadline,
    )

    achieved_at = datetime.now()

    project.mark_achieved(achieved_at)

    assert project.achieved_at == achieved_at
    assert project.achieved_on_time is True
