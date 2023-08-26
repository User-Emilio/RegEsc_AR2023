from . import bp_profesores
from sqlalchemy.exc import OperationalError

# Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import send_file

# Controladores


@bp_profesores.route('/profesor')
def handle_profesor():

    return "Route Profesor OK"