from flask import Blueprint, request, jsonify
from .. import db
from ..models import Exercise, Subject
from ..schemas import ExerciseSchema

exercise_bp = Blueprint('exercise', __name__)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

@exercise_bp.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json() or {}
    try:
        exercise = exercise_schema.load(data, session=db.session)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    db.session.add(exercise)
    db.session.commit()
    return jsonify({'status': 'success', 'data': exercise_schema.dump(exercise)}), 201

@exercise_bp.route('/exercises', methods=['GET'])
def list_exercises():
    exercises = Exercise.query.all()
    return jsonify({'status': 'success', 'data': exercises_schema.dump(exercises)}), 200

@exercise_bp.route('/exercises/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    return jsonify({'status': 'success', 'data': exercise_schema.dump(exercise)}), 200

@exercise_bp.route('/exercises/<int:exercise_id>', methods=['PUT'])
def update_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    data = request.get_json() or {}
    try:
        exercise = exercise_schema.load(data, instance=exercise, session=db.session, partial=True)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    db.session.commit()
    return jsonify({'status': 'success', 'data': exercise_schema.dump(exercise)}), 200

@exercise_bp.route('/exercises/<int:exercise_id>', methods=['DELETE'])
def delete_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({'status': 'success', 'data': {'id': exercise_id}}), 200
