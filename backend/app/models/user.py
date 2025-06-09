from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    __mapper_args__ = {
        'polymorphic_on': 'role',
        'polymorphic_identity': 'user'
    }

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Werkzeug 3.x usa scrypt por defecto para generar los hashes, los cuales
    # superan los 128 caracteres. Aumentamos el tamaño del campo para evitar
    # errores de truncamiento al registrar usuarios.
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')  # 'student' o 'admin'
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
