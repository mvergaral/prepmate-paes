from .. import db

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    area = db.Column(db.String(120), nullable=True)

    exercises = db.relationship('Exercise', back_populates='subject', cascade='all, delete-orphan')
