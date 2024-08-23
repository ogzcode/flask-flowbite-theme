from app import db
from app.models import User

class UserServices:
    @staticmethod
    def create_user(username, email, password):
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def delete_user_by_id(id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return User.query.all()