from datetime import datetime
from .. import db

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    options = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.String(5), nullable=False)
    difficulty = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    subject = db.relationship('Subject', back_populates='exercises')
    assignments = db.relationship(
        'Assignment', back_populates='exercise', cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'difficulty': self.difficulty,
            'tags': self.tags,
            'subject_id': self.subject_id,
        }
