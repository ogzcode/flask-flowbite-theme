from flask import Blueprint, render_template
from flask_login import login_required

dashboard_routes = Blueprint('dashboard_routes', __name__)


@dashboard_routes.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('pages/dashboard.html')

