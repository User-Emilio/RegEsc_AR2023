# Flask Form
from flask_wtf import FlaskForm

# Fields
from wtforms.fields import StringField
from wtforms.fields import PasswordField
from wtforms.fields import SubmitField

# Validators
from wtforms.validators import DataRequired
from wtforms.validators import Length

class LoginForm(FlaskForm):

    username = StringField('Usuario',validators=[DataRequired(message='Ingrese Usuario'),Length(min=1,max=19)])
    dni = StringField('DNI',validators=[DataRequired(message="Ingrese DNI."),Length(min=8,max=8)])
    password = PasswordField('Contraseña',validators=[DataRequired(message='Ingrese Contraseña'),Length(min=6,max=20)])
    submit = SubmitField('Iniciar Sesion')

    