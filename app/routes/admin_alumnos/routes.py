from . import bp_alumnos
from sqlalchemy.exc import OperationalError


# Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import send_file
from flask import request

# Flask Login
from flask_login import current_user
from flask_login import login_required

# Controladores
from ...controllers.controller_alumno import Alumno


@bp_alumnos.route('/alumno',methods=['GET'])
@login_required
def handle_alumno():

    #alumno = Alumno(current_user)

    return render_template('admin_alumnos/alumno.html')