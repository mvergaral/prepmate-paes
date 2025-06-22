from .conftest import BaseTestCase, UserFactory
from flask import json
from flask_jwt_extended import create_access_token

class TestSubjectEndpoints(BaseTestCase):
    def test_subject_crud(self):
        with self.app.app_context():
            admin, _ = UserFactory.create_admin()
            token = create_access_token(identity=str(admin.id))

            payload = {"name": "Matemática", "description": "desc", "area": "Math"}
            res = self.client.post('/subjects', json=payload, headers={'Authorization': f'Bearer {token}'})
            self.assertEqual(res.status_code, 201)
            data = json.loads(res.data)
            subject_id = data['data']['id']

            res = self.client.get('/subjects')
            self.assertEqual(res.status_code, 200)
            data_list = json.loads(res.data)
            self.assertEqual(len(data_list['data']), 1)

            res = self.client.get(f'/subjects/{subject_id}')
            self.assertEqual(res.status_code, 200)

            res = self.client.put(
                f'/subjects/{subject_id}',
                json={"name": "Mate"},
                headers={'Authorization': f'Bearer {token}'}
            )
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertEqual(data['data']['name'], 'Mate')

            res = self.client.delete(
                f'/subjects/{subject_id}',
                headers={'Authorization': f'Bearer {token}'}
            )
            self.assertEqual(res.status_code, 200)

            res = self.client.get(f'/subjects/{subject_id}')
            self.assertEqual(res.status_code, 404)
