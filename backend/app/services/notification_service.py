from datetime import datetime, timedelta
from app.models.assignment import Assignment


def get_notification_for_user(user_id: int):
    last = (
        Assignment.query.filter_by(user_id=user_id)
        .order_by(Assignment.created_at.desc())
        .first()
    )
    if not last:
        return "¡Comienza a practicar tus ejercicios hoy!"
    if datetime.utcnow() - last.created_at > timedelta(days=7):
        return "Hace tiempo que no practicas, ¡sigue estudiando!"
    return None
