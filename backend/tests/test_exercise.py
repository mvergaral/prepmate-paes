from .conftest import BaseTestCase
from flask import json

class TestExerciseEndpoints(BaseTestCase):
    def test_exercise_crud(self):
        with self.app.app_context():
            # create subject first
            s_res = self.client.post('/subjects', json={"name": "Ciencias", "description": "desc", "area": "Science"})
            subject_id = json.loads(s_res.data)['data']['id']

            payload = {
                "title": "Pregunta 1",
                "description": "desc",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "correct_answer": "A",
                "subject_id": subject_id,
                "difficulty": "easy",
                "tags": "tag1"
            }
            res = self.client.post('/exercises', json=payload)
            self.assertEqual(res.status_code, 201)
            data = json.loads(res.data)
            exercise_id = data['data']['id']

            res = self.client.get('/exercises')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(json.loads(res.data)['data']), 1)

            res = self.client.put(f'/exercises/{exercise_id}', json={"difficulty": "medium"})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(json.loads(res.data)['data']['difficulty'], 'medium')

            res = self.client.delete(f'/exercises/{exercise_id}')
            self.assertEqual(res.status_code, 200)
            res = self.client.get(f'/exercises/{exercise_id}')
            self.assertEqual(res.status_code, 404)
