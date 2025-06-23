from .conftest import BaseTestCase, UserFactory
from app.models import Subject, Exercise, Assignment
from flask import json
from flask_jwt_extended import create_access_token
from app import db


class TestProgressAPI(BaseTestCase):
    def setUp(self):
        super().setUp()
        with self.app.app_context():
            self.user, _ = UserFactory.create_student(email='prog@test.com')
            self.user_id = self.user.id
            self.token = create_access_token(identity=str(self.user_id))

            subject = Subject(name='Matematica')
            db.session.add(subject)
            db.session.commit()
            exercise = Exercise(
                title='q1',
                options={'A': '1'},
                correct_answer='A',
                subject_id=subject.id,
            )
            db.session.add(exercise)
            db.session.commit()
            assignment = Assignment(
                user_id=self.user_id,
                exercise_id=exercise.id,
                subject_id=subject.id,
                respuesta_entregada='A',
                correcta=True,
            )
            db.session.add(assignment)
            db.session.commit()

    def test_user_progress(self):
        with self.app.app_context():
            res = self.client.get(
                f'/api/progress/{self.user_id}',
                headers={'Authorization': f'Bearer {self.token}'},
            )
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.data)
            self.assertEqual(data['progress'][0]['correct'], 1)

    def test_progress_counts_unique_exercises(self):
        """A repeated assignment for the same exercise should not increase totals."""
        with self.app.app_context():
            subject = Subject.query.first()
            exercise = Exercise.query.first()
            repeat = Assignment(
                user_id=self.user_id,
                exercise_id=exercise.id,
                subject_id=subject.id,
                respuesta_entregada='A',
                correcta=True,
            )
            db.session.add(repeat)
            db.session.commit()

            res = self.client.get(
                f'/api/progress/{self.user_id}',
                headers={'Authorization': f'Bearer {self.token}'},
            )
            data = json.loads(res.data)
            self.assertEqual(data['progress'][0]['total'], 1)
            self.assertEqual(data['progress'][0]['correct'], 1)
