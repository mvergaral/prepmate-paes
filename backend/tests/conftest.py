import unittest
from app import create_app, db
from app.models import User, Student, Admin

default_student_kwargs = dict(name='Test', rut='1-9', age=18)
default_admin_kwargs = dict(name='Admin', rut='3-3', age=30, accepted_terms=True)

class UserFactory:
    @staticmethod
    def create_student(email='student@test.com', password='1234', **kwargs):
        student = Student(email=email, role='student', **{**default_student_kwargs, **kwargs})
        student.set_password(password)
        db.session.add(student)
        db.session.commit()
        return student, student

    @staticmethod
    def create_admin(email='admin@test.com', password='adminpass', **kwargs):
        admin = Admin(email=email, role='admin', **{**default_admin_kwargs, **kwargs})
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        return admin, admin

    @staticmethod
    def create_user(email='user@test.com', password='1234', role='student'):
        user = User(email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:', 'TESTING': True})
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
