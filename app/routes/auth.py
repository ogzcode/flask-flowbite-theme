from flask import Blueprint, request, jsonify, render_template, redirect, url_for

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
