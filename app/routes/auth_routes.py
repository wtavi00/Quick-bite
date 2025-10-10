from flask import Blueprint, request, jsonify
from app.models.user import User, db
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"msg": "username & password required"}), 400

    existing = User.query.filter_by(username=username).first()
    if existing:
        return jsonify({"msg": "username already taken"}), 409

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "user created", "user_id": user.id}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"msg": "Bad credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"access_token": token}), 200
