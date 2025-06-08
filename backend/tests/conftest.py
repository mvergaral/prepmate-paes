import unittest
from app import create_app, db
from app.models import User, Student, Admin

default_student_kwargs = dict(name='Test', rut='1-9', age=18)
default_admin_kwargs = dict(name='Admin', rut='3-3', age=30, accepted_terms=True)

class UserFactory:
    @staticmethod
    def create_student(email='student@test.com', password='1234', **kwargs):
        user = User(email=email, role='student')
        user.set_password(password)
        db.session.add(user)
        db.session.flush()
        student = Student(id=user.id, **{**default_student_kwargs, **kwargs})
        db.session.add(student)
        db.session.commit()
        return user, student

    @staticmethod
    def create_admin(email='admin@test.com', password='adminpass', **kwargs):
        user = User(email=email, role='admin')
        user.set_password(password)
        db.session.add(user)
        db.session.flush()
        admin = Admin(id=user.id, **{**default_admin_kwargs, **kwargs})
        db.session.add(admin)
        db.session.commit()
        return user, admin

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
