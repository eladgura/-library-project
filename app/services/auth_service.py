from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import db
from app.models.user import User

class AuthService:
    @staticmethod
    def register_user(data):
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
            return {"message": "User already exists"}, 409

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

    @staticmethod
    def login_user(data):
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity={'username': user.username, 'is_admin': user.is_admin})
            return {'access_token': access_token}, 200

        return {"message": "Invalid credentials"}, 401
