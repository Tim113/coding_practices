from app_name.database import db
from flask_security import Security, SQLAlchemyUserDatastore, LoginForm
from flask import jsonify
import app_name.auth.models

security = Security()

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)


def init_app(app):
    # Setup Flask-Security
    security._state = security.init_app(app, user_datastore)

    # to enable token based authentication
    # https://github.com/mattupstate/flask-security/issues/30
    # @app.route('/login_csrf')
    # def login_csrf():
    #     form = LoginForm()
    #     return jsonify({'csrf_token': form.csrf_token.current_token})
