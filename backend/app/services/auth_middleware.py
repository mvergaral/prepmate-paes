from functools import wraps
from flask import request, jsonify, g
from flask_jwt_extended import decode_token, get_jwt_identity
from flask_jwt_extended.exceptions import NoAuthorizationError, ExpiredSignatureError, InvalidHeaderError
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from werkzeug.exceptions import Unauthorized
from flask import current_app
from datetime import datetime, timezone
import redis


# Configuración de Redis (ajusta el host/puerto según tu entorno)
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

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
            jti = get_jwt()['jti']
            exp = get_jwt().get('exp')
            if is_token_blacklisted(jti):
                return jsonify({'message': 'Token revocado'}), 401
            g.user = user
        except ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except (NoAuthorizationError, InvalidHeaderError):
            return jsonify({'message': 'Token inválido'}), 401
        except Exception as e:
            return jsonify({'message': 'Error de autenticación', 'error': str(e)}), 401
        return fn(*args, **kwargs)
    return wrapper
