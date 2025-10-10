from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

from app.models.user import db as user_db
from app.routes.auth_routes import auth
# import other blueprints: orders, restaurants, etc.

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///quickbite.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "super-secret-key")

    # Init extensions
    user_db.init_app(app)
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth)
    # register other blueprints

    @app.route('/')
    def health_check():
        return {"status": "Quickbite API running"}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
