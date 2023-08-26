from . import bp_alumnos
from sqlalchemy.exc import OperationalError


# Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import send_file

# Controladores


@bp_alumnos.route('/alumno')
def handle_alumno():

    return "Route Alumno OK"