from . import db

class Preceptor(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    apellido = db.Column(db.String,nullable=False)

    def __repr__(self):

        return "<Preceptor: {},{} >".format(self.nombre,self.apellido)