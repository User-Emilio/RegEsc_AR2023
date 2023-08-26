from flask import Blueprint

bp_alumnos = Blueprint('alumnos',__name__,template_folder='../views/templates')

from . import routes