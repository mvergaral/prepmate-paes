from flask import Blueprint, jsonify, g
from app.models.user import User
from app import db
from app.services.auth_middleware import jwt_required, admin_required
from app.schemas import UserSchema
from app.services.progress_service import get_progress_by_user

admin_bp = Blueprint('admin_api', __name__)
user_schema = UserSchema(many=True)

@admin_bp.route('/api/admin/users', methods=['GET'])
@jwt_required
@admin_required
def list_users():
    users = User.query.all()
    return jsonify({'users': user_schema.dump(users)}), 200

@admin_bp.route('/api/admin/users/<int:user_id>/deactivate', methods=['POST'])
@jwt_required
@admin_required
def deactivate_user(user_id):
    user = User.query.get_or_404(user_id)
    user.is_active = False
    db.session.commit()
    return jsonify({'message': 'Usuario desactivado'}), 200

@admin_bp.route('/api/admin/users/<int:user_id>/progress', methods=['GET'])
@jwt_required
@admin_required
def user_progress_admin(user_id):
    progress = get_progress_by_user(user_id)
    return jsonify({'progress': progress}), 200
