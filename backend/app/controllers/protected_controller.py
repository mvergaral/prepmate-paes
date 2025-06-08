from flask import Blueprint, jsonify, g
from ..services.auth_middleware import jwt_required

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/me', methods=['GET'])
def me():
    user = g.user
    return jsonify({
        'id': user.id,
        'email': user.email,
        'role': user.role,
        'is_active': user.is_active
    })
