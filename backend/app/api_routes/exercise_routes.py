from flask import Blueprint, request, jsonify
from app.services.exercise_service import get_exercises_by_subject

exercise_bp = Blueprint('exercise_api', __name__)


@exercise_bp.route('/api/exercises', methods=['GET'])
def get_exercises():
    materia = request.args.get('materia')
    exercises = get_exercises_by_subject(materia)
    return jsonify([e.to_dict() for e in exercises]), 200
