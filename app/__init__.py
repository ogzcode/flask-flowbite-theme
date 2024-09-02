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
login_manager.login_view = 'auth_routes.login' 


from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.routes import auth_routes, dashboard_routes, e_commerce_routes

app.register_blueprint(auth_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(e_commerce_routes)



from app.cli import seed_products, clear_products

app.cli.add_command(seed_products)
app.cli.add_command(clear_products)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)