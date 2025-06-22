from flask import Blueprint, jsonify, g
from app.services.auth_middleware import jwt_required
from app.services.progress_service import get_progress_by_user

progress_bp = Blueprint('progress_api', __name__)

@progress_bp.route('/api/progress/<int:user_id>', methods=['GET'])
@jwt_required
def user_progress(user_id):
    user = g.user
    if user.id != user_id and user.role != 'admin':
        return jsonify({'message': 'No autorizado'}), 403

    progress = get_progress_by_user(user_id)
    return jsonify({'progress': progress}), 200
