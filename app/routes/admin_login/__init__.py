from flask import Blueprint

bp_login = Blueprint('login',__name__,template_folder='../views/templates')

from . import routes