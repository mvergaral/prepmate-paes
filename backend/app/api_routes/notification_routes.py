from flask import Blueprint, jsonify, g
from app.services.auth_middleware import jwt_required
from app.services.notification_service import get_notification_for_user

notification_bp = Blueprint('notification_api', __name__)

@notification_bp.route('/api/notifications', methods=['GET'])
@jwt_required
def get_notifications():
    message = get_notification_for_user(g.user.id)
    return jsonify({'message': message or ''}), 200
