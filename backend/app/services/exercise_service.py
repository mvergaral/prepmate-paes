from app.models.exercise import Exercise

def get_exercises_by_subject(materia: str, difficulty: str | None = None):
    query = Exercise.query.join(Exercise.subject).filter_by(name=materia)
    if difficulty:
        query = query.filter(Exercise.difficulty == difficulty)
    return query.all()
