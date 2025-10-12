import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///quickbite.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "change-this-secret")

    db.init_app(app)
    jwt = JWTManager(app)

    from app.routes.auth_routes import auth
    app.register_blueprint(auth, url_prefix="/api/auth")

    @app.route("/healthz")
    def health_check():
        return {"status": "Quickbite API running"}, 200

    return app


if __name__ == "__main__":
    app = create_app()
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
