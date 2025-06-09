import unittest
from app import create_app, db
from app.models import User, Student
from flask import json
from flask_jwt_extended import create_access_token
from .conftest import BaseTestCase, UserFactory

class TestProfileEndpoints(BaseTestCase):
    def setUp(self):
        super().setUp()
        with self.app.app_context():
            self.user, self.student = UserFactory.create_student(email='profile@test.com', rut='9-9', name='Profile', age=22)
            self.token = create_access_token(identity=str(self.user.id))

    def test_create_profile_missing_fields(self):
        with self.app.app_context():
            res = self.client.post('/profile',
                headers={'Authorization': f'Bearer {self.token}'},
                json={})
            self.assertEqual(res.status_code, 400)

    def test_update_profile(self):
        with self.app.app_context():
            res = self.client.put('/profile',
                headers={'Authorization': f'Bearer {self.token}'},
                json={'name': 'Nuevo Nombre', 'colegio': 'Colegio X'})
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertEqual(data['student']['name'], 'Nuevo Nombre')
            self.assertEqual(data['student']['colegio'], 'Colegio X')

    def test_profile_requires_auth(self):
        with self.app.app_context():
            res = self.client.put('/profile', json={'name': 'X'})
            self.assertEqual(res.status_code, 401)

    def test_get_profile_success(self):
        with self.app.app_context():
            res = self.client.get('/profile',
                headers={'Authorization': f'Bearer {self.token}'}
            )
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertEqual(data['student']['name'], 'Profile')

    def test_get_profile_not_found(self):
        with self.app.app_context():
            user = UserFactory.create_user(email='no_profile@test.com')
            token = create_access_token(identity=str(user.id))
            res = self.client.get('/profile', headers={'Authorization': f'Bearer {token}'})
            self.assertEqual(res.status_code, 404)

    def test_get_profile_requires_auth(self):
        with self.app.app_context():
            res = self.client.get('/profile')
            self.assertEqual(res.status_code, 401)

    def test_create_profile_success(self):
        with self.app.app_context():
            # Crear un usuario sin perfil para probar creación
            payload = {
                'name': 'Nuevo',
                'rut': '10-1',
                'age': 25,
                'colegio': 'Colegio Test',
                'comuna': 'Comuna Test',
                'region': 'Región Test',
                'accepted_terms': True
            }
            res = self.client.post('/profile',
                headers={'Authorization': f'Bearer {self.token}'},
                json=payload)
            self.assertEqual(res.status_code, 400)

if __name__ == '__main__':
    unittest.main()
