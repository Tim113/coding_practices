import os
from flask import Flask, redirect, url_for
from flask_security import login_required

# Initialising variables
app = None

import app_name.database
from app_name import auth
from app_name.config import config

from app_name.homepage.views import homepage_blueprint

def create_app(name, environment=None):

    # Select config mode
    if environment is None:
        environment = 'development'

    # Create Flask app
    app = Flask(name, template_folder='app_name/templates', static_folder='app_name/static')

    app.config.from_object(config[environment])
    app.config.from_envvar('envvar_config', silent=True)
    
    return app


def get_app(name, environment=None):
    app = create_app(name, environment)

    # initiate extentions
    database.db.init_app(app)
    auth.init_app(app)

    # Initiate extentions
    app.register_blueprint(homepage_blueprint, url_prefix='/home')

    @app.route('/')
    @login_required
    def index():
        return redirect(url_for('homepage_blueprint.homepage_index'))

    app.secret_key = app.config['SECRET_KEY']

    return app


if __name__ == '__main__':
    app = get_app(__name__)
    app.run(debug=app.config['APP_DEBUG'])