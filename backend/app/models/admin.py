from .. import db
from .user import User

class Admin(User):
    __tablename__ = 'admins'
    __mapper_args__ = {'polymorphic_identity': 'admin'}
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    # Puedes agregar campos específicos de admin aquí si es necesario
