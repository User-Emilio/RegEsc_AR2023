from . import db
from . import bcrypt
from . import login_manager

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    # Try catch
    # Si la consulta falla controlar la excepcion

    usuario = Usuario.query.get(int(user_id))

    return usuario


class Usuario(db.Model, UserMixin):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    dni = db.Column(db.String(9),nullable=False)
    hash_password = db.Column(db.String(128),nullable=False)
    tipo_cuenta = db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return "<Usuario: {}".format(self.username)

    def encrypt_password(self,password):
        self.hash_password = bcrypt.generate_password_hash(password)

    def check_password(self,password):
        return bcrypt.check_password_hash(self.hash_password,password)