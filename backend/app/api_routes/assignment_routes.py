from flask import Blueprint, request, jsonify
from app.models.assignment import Assignment
from app.models.exercise import Exercise
from app import db

assignment_bp = Blueprint('assignment_api', __name__)


@assignment_bp.route('/api/assignments', methods=['POST'])
def submit_assignment():
    data = request.json or {}
    exercise = Exercise.query.get(data.get('exercise_id'))
    assignment = Assignment(
        user_id=data.get('user_id'),
        exercise_id=data.get('exercise_id'),
        subject_id=exercise.subject_id if exercise else None,
        respuesta_entregada=data.get('respuesta_entregada'),
        correcta=data.get('correcta', False)
    )
    db.session.add(assignment)
    db.session.commit()
    return jsonify({"message": "Respuesta registrada"}), 201


@assignment_bp.route('/api/assignments', methods=['GET'])
def list_assignments():
    user_id = request.args.get('user_id', type=int)
    subject_id = request.args.get('subject_id', type=int)
    query = Assignment.query
    if user_id:
        query = query.filter_by(user_id=user_id)
    if subject_id:
        query = query.filter_by(subject_id=subject_id)
    assignments = query.order_by(Assignment.created_at.desc()).all()
    return (
        jsonify([a.to_dict() for a in assignments]),
        200,
    )
