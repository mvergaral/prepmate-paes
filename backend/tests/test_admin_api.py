from .conftest import BaseTestCase, UserFactory
from app.models import User
from flask_jwt_extended import create_access_token
from flask import json
from app import db


class TestAdminAPI(BaseTestCase):
    def setUp(self):
        super().setUp()
        with self.app.app_context():
            self.admin, _ = UserFactory.create_admin(email='admin@tests.com')
            self.user, _ = UserFactory.create_student(email='std@test.com')
            self.user_id = self.user.id
            self.admin_token = create_access_token(identity=str(self.admin.id))

    def test_list_users(self):
        with self.app.app_context():
            res = self.client.get(
                '/api/admin/users',
                headers={'Authorization': f'Bearer {self.admin_token}'},
            )
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertGreaterEqual(len(data['users']), 2)

    def test_deactivate_user(self):
        with self.app.app_context():
            res = self.client.post(
                f'/api/admin/users/{self.user_id}/deactivate',
                headers={'Authorization': f'Bearer {self.admin_token}'},
            )
            self.assertEqual(res.status_code, 200)
            reloaded = User.query.get(self.user_id)
            self.assertFalse(reloaded.is_active)
