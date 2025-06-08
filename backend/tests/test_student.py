from .conftest import BaseTestCase, UserFactory
from app.models import Student

class StudentModelTest(BaseTestCase):
    def test_student_creation(self):
        with self.app.app_context():
            _, student = UserFactory.create_student(email='student@x.com', name='Alumno', rut='4-4', age=19)
            assert student.name == 'Alumno'
            assert student.rut == '4-4'
            assert student.age == 19
