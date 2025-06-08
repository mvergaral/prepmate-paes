from functools import wraps
from flask import request, jsonify, g
from flask_jwt_extended import decode_token, get_jwt_identity
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from werkzeug.exceptions import Unauthorized
from flask import current_app
from datetime import datetime, timezone
import redis
import os


# Configuración de Redis (ajusta el host/puerto según tu entorno)
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

BLACKLIST_PREFIX = 'jwt_blacklist:'


def add_token_to_blacklist(jti, exp=None):
    key = BLACKLIST_PREFIX + jti
    # Si se pasa la expiración, usarla para el TTL
    if exp:
        ttl = int(exp - datetime.now(timezone.utc).timestamp())
        redis_client.setex(key, ttl, 'revoked')
    else:
        redis_client.set(key, 'revoked')


def is_token_blacklisted(jti):
    key = BLACKLIST_PREFIX + jti
    return redis_client.exists(key)


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'message': 'Token de autenticación requerido'}), 401
        try:
            verify_jwt_in_request()
            from ..models.user import User
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if not user:
                return jsonify({'message': 'Usuario no encontrado'}), 401
            # Blacklist check
            jwt_data = get_jwt()
            jti = jwt_data['jti']
            exp = jwt_data.get('exp')
            if is_token_blacklisted(jti):
                return jsonify({'message': 'Token revocado'}), 401
            g.user = user
            return fn(*args, **kwargs)
        except (NoAuthorizationError, InvalidHeaderError):
            return jsonify({'message': 'Token inválido o expirado'}), 401
        except Exception as e:
            current_app.logger.error('Unhandled exception during authentication: %s', str(e))
            return jsonify({'message': 'Error de autenticación'}), 401
    return wrapper
