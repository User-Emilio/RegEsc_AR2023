# Modelos
from ..models.usuario import Usuario

# Flask Login
from flask_login import login_user

def usuarioCorrecto(form):

    usuario = Usuario.query.filter_by(username=form.username.data,dni=form.dni.data).first()

    if usuario and usuario.check_password(form.password.data):
        login_user(usuario)

        return usuario
    
    else:
        return None
        