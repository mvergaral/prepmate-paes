from flask import Blueprint, request, jsonify, g
from ..services.auth_middleware import jwt_required
from ..models import Student
from ..schemas import StudentSchema
from .. import db

profile_bp = Blueprint('profile', __name__)
student_schema = StudentSchema()

@profile_bp.route('/profile', methods=['POST'])
@jwt_required
def create_profile():
    user = g.user
    if user.role != 'student':
        return jsonify({'message': 'Solo los estudiantes pueden crear perfil'}), 403
    data = request.get_json() or {}
    required_fields = ['name', 'rut', 'age', 'colegio', 'comuna', 'region']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Faltan campos requeridos'}), 400
    # Verificar si ya existe perfil
    if Student.query.filter_by(id=user.id).first():
        return jsonify({'message': 'El perfil ya existe'}), 400
    db.session.execute(
        Student.__table__.insert().values(
            id=user.id,
            name=data['name'],
            rut=data['rut'],
            age=data['age'],
            colegio=data['colegio'],
            comuna=data['comuna'],
            region=data['region'],
            accepted_terms=data.get('accepted_terms', False)
        )
    )
    db.session.commit()
    db.session.expunge(user)
    db.session.expire_all()
    student = Student.query.get(user.id)
    return jsonify({'student': student_schema.dump(student)}), 201

@profile_bp.route('/profile', methods=['PUT'])
@jwt_required
def update_profile():
    user = g.user
    if user.role != 'student':
        return jsonify({'message': 'Solo los estudiantes pueden modificar perfil'}), 403
    data = request.get_json() or {}
    student = Student.query.filter_by(id=user.id).first()
    if not student:
        return jsonify({'message': 'Perfil no encontrado'}), 404
    for field in ['name', 'rut', 'age', 'colegio', 'comuna', 'region']:
        if field in data:
            setattr(student, field, data[field])
    db.session.commit()
    return jsonify({'student': student_schema.dump(student)}), 200
