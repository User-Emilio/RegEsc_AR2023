from flask import Blueprint

bp_preceptores = Blueprint('preceptores',__name__,template_folder='../views/templates')

from . import routes