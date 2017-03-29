from flask import render_template, Blueprint

homepage_blueprint = Blueprint('homepage_blueprint', __name__)


@homepage_blueprint.route('/')
def homepage_index():

    return render_template('index.html')
