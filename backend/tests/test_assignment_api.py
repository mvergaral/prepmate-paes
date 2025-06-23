from .conftest import BaseTestCase, UserFactory
from flask import json
from flask_jwt_extended import create_access_token

class TestAssignmentAPI(BaseTestCase):
    def test_exercise_query_and_assignment(self):
        with self.app.app_context():
            # create user
            student, _ = UserFactory.create_student()
            admin, _ = UserFactory.create_admin()
            token = create_access_token(identity=str(admin.id))
            # create subject and exercise
            s_res = self.client.post('/subjects', json={"name": "Mate", "description": "desc", "area": "math"}, headers={'Authorization': f'Bearer {token}'})
            subject_id = json.loads(s_res.data)['data']['id']
            payload = {
                "title": "Pregunta 1",
                "options": {"A": "1", "B": "2"},
                "correct_answer": "A",
                "subject_id": subject_id
            }
            e_res = self.client.post('/exercises', json=payload, headers={'Authorization': f'Bearer {token}'})
            exercise_id = json.loads(e_res.data)['data']['id']

            res = self.client.get('/api/exercises?materia=Mate')
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertEqual(len(data), 1)

            assign_payload = {
                "user_id": student.id,
                "exercise_id": exercise_id,
                "respuesta_entregada": "A",
                "correcta": True
            }
            res = self.client.post('/api/assignments', json=assign_payload)
            self.assertEqual(res.status_code, 201)

            res = self.client.get(f'/api/assignments?user_id={student.id}&subject_id={subject_id}')
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['exercise_id'], exercise_id)
