from .conftest import BaseTestCase, UserFactory
from app.models import Admin

class TestAdminModel(BaseTestCase):
    def test_admin_creation(self):
        with self.app.app_context():
            _, admin = UserFactory.create_admin(email='admin2@admin.com', name='SuperAdmin', rut='5-5', age=40, accepted_terms=True)
            assert admin.name == 'SuperAdmin'
            assert admin.rut == '5-5'
            assert admin.age == 40
            assert admin.accepted_terms is True
