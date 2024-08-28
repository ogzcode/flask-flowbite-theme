from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlsplit

from app.services import UserServices

auth_routes = Blueprint('auth_routes', __name__, template_folder='templates')


@auth_routes.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_routes.dashboard'))

    if request.args.get('next') is not None:
        next_url = urlsplit(request.args.get('next'))
        if next_url.netloc == '':
            return redirect(url_for('auth_routes.login'))
        else:
            return redirect(url_for('index'))
        
    return render_template('pages/login.html')


@auth_routes.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json()

    user = UserServices.get_user_by_email(req_data['email'])

    if user is None or not user.check_password(req_data['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    login_user(user)

    return redirect(url_for('dashboard_routes.dashboard'))


@auth_routes.route('/register', methods=['GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_routes.dashboard'))

    return render_template('pages/register.html')


@auth_routes.route('/register', methods=['POST'])
def register_post():
    req_data = request.get_json()

    user = UserServices.get_user_by_email(req_data['email'])

    if user is not None:
        return jsonify({"error": "User already exists"}), 400

    UserServices.create_user(
        username=req_data['username'],
        email=req_data['email'],
        password=req_data['password']
    )

    return jsonify({"message": "User created successfully"}), 201


@auth_routes.route('/forget-password', methods=['GET'])
def forget_password():
    return "hello"


@auth_routes.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_routes.login'))
