from sqlalchemy import func, case
from app.models.assignment import Assignment
from app.models.exercise import Exercise
from app.models.subject import Subject
from app import db


def get_progress_by_user(user_id: int):
    results = (
        db.session.query(
            Subject.name.label('subject'),
            func.count(Assignment.id).label('total'),
            func.sum(case((Assignment.correcta == True, 1), else_=0)).label('correct'),
        )
        .join(Exercise, Exercise.id == Assignment.exercise_id)
        .join(Subject, Subject.id == Exercise.subject_id)
        .filter(Assignment.user_id == user_id)
        .group_by(Subject.name)
        .all()
    )

    return [
        {'subject': r.subject, 'total': int(r.total), 'correct': int(r.correct or 0)}
        for r in results
    ]
