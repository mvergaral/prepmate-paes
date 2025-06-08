from .conftest import BaseTestCase, UserFactory
from app.models import User, Student, Admin

class TestUserModel(BaseTestCase):
    def test_password_hashing(self):
        with self.app.app_context():
            user, _ = UserFactory.create_student(email='a@b.com', password='1234')
            assert user.check_password('1234')
            assert not user.check_password('wrong')

class TestStudentModel(BaseTestCase):
    def test_student_creation(self):
        with self.app.app_context():
            student, _ = UserFactory.create_student(email='b@b.com', name='Estudiante', rut='2-7', age=20)
            assert student.name == 'Estudiante'
            assert student.rut == '2-7'
            assert student.age == 20

class TestAdminModel(BaseTestCase):
    def test_admin_creation(self):
        with self.app.app_context():
            admin, _ = UserFactory.create_admin(email='admin@admin.com', name='Admin', rut='3-3', age=30, accepted_terms=True)
            assert admin.name == 'Admin'
            assert admin.rut == '3-3'
            assert admin.age == 30
            assert admin.accepted_terms is True
