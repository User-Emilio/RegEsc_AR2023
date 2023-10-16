from . import bp_preceptores
from sqlalchemy.exc import OperationalError

# Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import send_file

# Controladores

@bp_preceptores.route('/preceptor')
def handle_preceptor():

    return render_template('admin_preceptores/preceptor.html')