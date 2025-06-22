from flask import Blueprint, request, jsonify
from app.models.assignment import Assignment
from app import db

assignment_bp = Blueprint('assignment_api', __name__)


@assignment_bp.route('/api/assignments', methods=['POST'])
def submit_assignment():
    data = request.json or {}
    assignment = Assignment(
        user_id=data.get('user_id'),
        exercise_id=data.get('exercise_id'),
        respuesta_entregada=data.get('respuesta_entregada'),
        correcta=data.get('correcta', False)
    )
    db.session.add(assignment)
    db.session.commit()
    return jsonify({"message": "Respuesta registrada"}), 201
