from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

from app.routes import auth_routes

app.register_blueprint(auth_routes)

@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)