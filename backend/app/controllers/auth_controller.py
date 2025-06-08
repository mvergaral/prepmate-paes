from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt
from .. import db
from ..models import Student, User, Admin
from ..schemas import StudentSchema, UserSchema, AdminSchema
from ..services.auth_middleware import jwt_required, add_token_to_blacklist

auth_bp = Blueprint('auth', __name__)
student_schema = StudentSchema()
admin_schema = AdminSchema()
user_schema = UserSchema()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    if 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing credentials'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    # Si es estudiante, obtener datos de Student
    student = Student.query.filter_by(id=user.id).first() if user.role == 'student' else None
    token = create_access_token(identity=user.id)
    response = {'access_token': token, 'user': user_schema.dump(user)}
    if student:
        response['student'] = student_schema.dump(student)
    return jsonify(response), 200

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}
    required_fields = ['name', 'email', 'password', 'rut', 'age']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing fields'}), 400

    # Verificar si el email ya existe en User
    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'Email already registered'}), 400

    # Crear usuario base con rol student
    user = User(
        email=data['email'],
        role='student'
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.flush()  # Para obtener user.id

    # Crear instancia Student enlazada al User
    student = Student(
        id=user.id,  # Hereda el id del User
        name=data['name'],
        rut=data['rut'],
        age=data['age'],
        accepted_terms=data.get('terms', False)
    )
    db.session.add(student)
    db.session.commit()

    token = create_access_token(identity=user.id)
    return jsonify({'access_token': token, 'user': user_schema.dump(user), 'student': student_schema.dump(student)}), 201

@auth_bp.route('/signup-admin', methods=['POST'])
def signup_admin():
    data = request.get_json() or {}
    required_fields = ['email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing fields'}), 400

    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'Email already registered'}), 400

    user = User(
        email=data['email'],
        role='admin'
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.flush()  # Save user and retrieve user.id without committing

    # Crear instancia Admin enlazada al User
    admin = Admin(
        id=user.id,  # Hereda el id del User
        name=data['name'],
        rut=data['rut'],
        age=data['age'],
        accepted_terms=data.get('terms', False)
    )
    db.session.add(admin)
    db.session.commit()

    token = create_access_token(identity=user.id)
    return jsonify({'access_token': token, 'user': user_schema.dump(user), 'admin': admin_schema.dump(admin)}), 201

@auth_bp.route('/logout', methods=['POST'])
@jwt_required
def logout():
    jwt_data = get_jwt()
    jti = jwt_data['jti']
    exp = jwt_data.get('exp')
    add_token_to_blacklist(jti, exp)
    return jsonify({'message': 'Sesión cerrada correctamente'}), 200
