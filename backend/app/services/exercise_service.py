from app.models.exercise import Exercise


def get_exercises_by_subject(materia: str):
    return Exercise.query.join(Exercise.subject).filter_by(name=materia).limit(10).all()
