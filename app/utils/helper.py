from app import login_manager
from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)