from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required

from app.services import UserServices

auth_routes = Blueprint('auth_routes', __name__, template_folder='templates')


@auth_routes.route('/login', methods=['GET'])
def login():
    return render_template('pages/login.html')


@auth_routes.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json()

    user = UserServices.get_user_by_email(req_data['email'])

    if user is None or not user.check_password(req_data['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    login_user(user)

    return redirect(url_for('home'))


@auth_routes.route('/register', methods=['GET'])
def register():
    return render_template('pages/register.html')


@auth_routes.route('/register', methods=['POST'])
def register_post():
    req_data = request.get_json()

    user = UserServices.get_user_by_email(req_data['email'])

    if user is not None:
        return jsonify({"error": "User already exists"}), 400

    UserServices.create_user(req_data)

    return redirect(url_for('auth_routes.login'))


@auth_routes.route('/forget-password', methods=['GET'])
def forget_password():
    return "hello"


@auth_routes.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_routes.login'))



