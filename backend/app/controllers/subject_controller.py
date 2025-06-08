from flask import Blueprint, request, jsonify
from .. import db
from ..models import Subject
from ..schemas import SubjectSchema

subject_bp = Blueprint('subject', __name__)
subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)

@subject_bp.route('/subjects', methods=['POST'])
def create_subject():
    data = request.get_json() or {}
    try:
        subject = subject_schema.load(data, session=db.session)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    db.session.add(subject)
    db.session.commit()
    return jsonify({'status': 'success', 'data': subject_schema.dump(subject)}), 201

@subject_bp.route('/subjects', methods=['GET'])
def list_subjects():
    subjects = Subject.query.all()
    return jsonify({'status': 'success', 'data': subjects_schema.dump(subjects)}), 200

@subject_bp.route('/subjects/<int:subject_id>', methods=['GET'])
def get_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    return jsonify({'status': 'success', 'data': subject_schema.dump(subject)}), 200

@subject_bp.route('/subjects/<int:subject_id>', methods=['PUT'])
def update_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    data = request.get_json() or {}
    try:
        subject = subject_schema.load(data, instance=subject, session=db.session, partial=True)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    db.session.commit()
    return jsonify({'status': 'success', 'data': subject_schema.dump(subject)}), 200

@subject_bp.route('/subjects/<int:subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    db.session.delete(subject)
    db.session.commit()
    return jsonify({'status': 'success', 'data': {'id': subject_id}}), 200
