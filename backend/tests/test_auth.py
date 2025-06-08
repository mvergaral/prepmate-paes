import unittest
from app import create_app, db
from flask import json
from .conftest import BaseTestCase, UserFactory

class TestAuthEndpoints(BaseTestCase):
    def setUp(self):
        super().setUp()
        with self.app.app_context():
            UserFactory.create_student(email='test@auth.com', password='1234')

    def test_login_success(self):
        with self.app.app_context():
            res = self.client.post('/auth/login', json={'email': 'test@auth.com', 'password': '1234'})
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertIn('access_token', data)

    def test_login_fail(self):
        with self.app.app_context():
            res = self.client.post('/auth/login', json={'email': 'test@auth.com', 'password': 'wrong'})
            self.assertEqual(res.status_code, 401)
