from sqlalchemy import func, case, Integer
from app.models.assignment import Assignment
from app.models.subject import Subject
from app import db


def get_progress_by_user(user_id: int):
    """Return progress grouped by subject counting each exercise once."""

    per_exercise = (
        db.session.query(
            Assignment.subject_id.label("subject_id"),
            Assignment.exercise_id.label("exercise_id"),
            func.max(case((Assignment.correcta, 1), else_=0)).label("correct"),
        )
        .filter(Assignment.user_id == user_id)
        .group_by(Assignment.subject_id, Assignment.exercise_id)
        .subquery()
    )

    results = (
        db.session.query(
            Subject.name.label("subject"),
            func.count(per_exercise.c.exercise_id).label("total"),
            func.sum(per_exercise.c.correct).label("correct"),
        )
        .join(Subject, Subject.id == per_exercise.c.subject_id)
        .group_by(Subject.name)
        .all()
    )

    return [
        {
            "subject": r.subject,
            "total": int(r.total),
            "correct": int(r.correct or 0),
        }
        for r in results
    ]
