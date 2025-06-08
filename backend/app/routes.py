from .controllers import auth_bp, protected_bp
from app.controllers.profile_controller import profile_bp


def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(protected_bp, url_prefix='/protected')
    app.register_blueprint(profile_bp)
