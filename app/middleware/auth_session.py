from datetime import datetime, timezone
from flask import session, redirect, url_for
from flask_login import current_user, logout_user
from app import app, login_manager

@app.before_request
def session_timeout():
    session.modified = True
    if current_user.is_authenticated and session.get('_permanent_session_start'):
        session_lifetime = app.permanent_session_lifetime.total_seconds()
        if (datetime.now(timezone.utc) - session['_permanent_session_start']).total_seconds() > session_lifetime:
            logout_user()
            return redirect(url_for('auth_routes.login'))

@app.after_request
def after_request(response):
    session['_permanent_session_start'] = datetime.now(timezone.utc)
    return response


@login_manager.unauthorized_handler
def unauthorized():
    print("Unauthorized")
    return redirect(url_for('auth_routes.login'))
