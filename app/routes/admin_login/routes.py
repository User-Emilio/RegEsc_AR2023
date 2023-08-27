from . import bp_login

# Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import send_file

# Flask Login
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user


# Forms
from ...forms.login_form import LoginForm

# Controladores
from ...controllers.controller_login import loginUsuario



@bp_login.route('/',methods=['GET','POST'])
@bp_login.route('/login',methods=['GET','POST'])
def handle_login():

    if current_user.is_authenticated:

        # Identificar que tipo de cuenta tiene el usuario
        # Redirigir a seccion correspondiente ---> PROFESOR | PRECEPTOR | ALUMNO

        print("CURRENT_USER: ",current_user)
        
        return redirect(url_for('alumnos.handle_alumno'))

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        
        # Si falla conexion con db capturar excepcion
        usuario = loginUsuario(form)

        if usuario:
            if usuario.tipo_cuenta == 'Alumno':
                return redirect(url_for('alumnos.handle_alumno'))
            elif usuario.tipo_cuenta == 'Preceptor':
                return redirect(url_for('preceptores.handle_preceptor'))
            elif usuario.tipo_cuenta == 'Profesor':
                return redirect(url_for('profesores.handle_profesor'))
            

    return render_template('admin_login/login.html',form=form)

@bp_login.route('/logout')
@login_required
def handle_logout():

    logout_user()

    return redirect(url_for('login.handle_login'))