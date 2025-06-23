from datetime import datetime
from .. import db

class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    respuesta_entregada = db.Column(db.String(255), nullable=False)
    correcta = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User')
    exercise = db.relationship('Exercise')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'exercise_id': self.exercise_id,
            'respuesta_entregada': self.respuesta_entregada,
            'correcta': self.correcta,
            'created_at': self.created_at.isoformat(),
            'subject_id': self.exercise.subject_id if self.exercise else None,
        }
