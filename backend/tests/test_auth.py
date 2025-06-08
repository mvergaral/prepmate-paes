import unittest
from app import create_app, db
from flask import json
from .conftest import BaseTestCase, UserFactory

class TestAuthEndpoints(BaseTestCase):
    def setUp(self):
        super().setUp()
        with self.app.app_context():
            self.user, _ = UserFactory.create_student(email='test@auth.com', password='1234')
            from flask_jwt_extended import create_access_token
            self.token = create_access_token(identity=self.user.id)

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

    def test_logout_revokes_token(self):
        with self.app.app_context():
            # Logout con el token válido
            res = self.client.post('/auth/logout', headers={'Authorization': f'Bearer {self.token}'})
            self.assertEqual(res.status_code, 200)
            # Intentar acceder a un endpoint protegido con el mismo token (debe ser rechazado)
            res2 = self.client.put('/profile', headers={'Authorization': f'Bearer {self.token}'}, json={'name': 'X'})
            self.assertEqual(res2.status_code, 401)
            # El mensaje de error debe indicar que el token fue revocado
            data = json.loads(res2.data)
            self.assertIn('revocado', data.get('message', ''))
