from flask import Flask
from flask_socketio import SocketIO

# Configuracion
from config import DevelopmentConfig

# Complementos
from .models import db
from .models import migrate
from .models import bcrypt

socketio = SocketIO()

def create_app():

    app = Flask(__name__,template_folder=DevelopmentConfig.TEMPLATE_FOLDER,static_folder=DevelopmentConfig.STATIC_FOLDER)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)

    #Blueprint / Vistas / Rutas de la Aplicacion
    
    from .routes.admin_preceptores import bp_preceptores
    app.register_blueprint(bp_preceptores)

    from .routes.admin_alumnos import bp_alumnos
    app.register_blueprint(bp_alumnos)

    from .routes.admin_profesores import bp_profesores
    app.register_blueprint(bp_profesores)
 
    socketio.init_app(app)

    return app