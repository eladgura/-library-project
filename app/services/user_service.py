from app import db
from app.models.user import User

class UserService:
    @staticmethod
    def get_users():
        users = User.query.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def get_user(id):
        user = User.query.get_or_404(id)
        return user.to_dict()

    @staticmethod
    def add_user(data):
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201

    @staticmethod
    def update_user(id, data):
        user = User.query.get_or_404(id)
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        user.is_admin = data.get('is_admin', user.is_admin)
        db.session.commit()
        return user.to_dict()

    @staticmethod
    def delete_user(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
