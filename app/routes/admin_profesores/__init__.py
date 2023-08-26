from flask import Blueprint

bp_profesores = Blueprint('profesores',__name__,template_folder='../views/templates')

from . import routes