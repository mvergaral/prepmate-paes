from .. import db
from .user import User

class Admin(User):
    __tablename__ = 'admins'
    __mapper_args__ = {'polymorphic_identity': 'admin'}
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    accepted_terms = db.Column(db.Boolean, default=False)
