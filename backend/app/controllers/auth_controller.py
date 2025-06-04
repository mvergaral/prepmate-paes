from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .. import db
from ..models import Student
from ..schemas import StudentSchema

auth_bp = Blueprint('auth', __name__)
student_schema = StudentSchema()

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}
    required_fields = ['name', 'email', 'password', 'rut', 'age']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing fields'}), 400

    if Student.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'Email already registered'}), 400

    student = Student(
        name=data['name'],
        email=data['email'],
        rut=data['rut'],
        age=data['age'],
        accepted_terms=data.get('terms', False)
    )
    student.set_password(data['password'])
    db.session.add(student)
    db.session.commit()

    token = create_access_token(identity=student.id)
    return jsonify({'access_token': token, 'student': student_schema.dump(student)}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    if 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing credentials'}), 400

    student = Student.query.filter_by(email=data['email']).first()
    if not student or not student.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = create_access_token(identity=student.id)
    return jsonify({'access_token': token, 'student': student_schema.dump(student)}), 200
