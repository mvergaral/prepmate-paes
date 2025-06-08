from .conftest import BaseTestCase
from app.models import User, Admin, db

class TestAdminModel(BaseTestCase):
    def test_admin_creation(self):
        with self.app.app_context():
            user = User(email='admin2@admin.com', role='admin')
            user.set_password('adminpass2')
            db.session.add(user)
            db.session.flush()
            admin = Admin(id=user.id, name='SuperAdmin', rut='5-5', age=40, accepted_terms=True)
            db.session.add(admin)
            db.session.commit()
            assert admin.name == 'SuperAdmin'
            assert admin.rut == '5-5'
            assert admin.age == 40
            assert admin.accepted_terms is True
