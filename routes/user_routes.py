"""
    Importing of packages
"""
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import db, User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/register', methods=['POST'])
def register_user():
    """
        Registering of users
    """
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    user_exists = User.query.filter_by(username=username).first()
    if user_exists:
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    try:
        new_user = User(username=username, email=email,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"Error": f"{e}"}), 500
