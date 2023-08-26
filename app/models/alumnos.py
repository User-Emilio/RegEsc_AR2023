from . import db

class Alumno(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    apellido = db.Column(db.String,nullable=False)
    dni = db.Column(db.String,nullable=False)
    año_curso = db.Column(db.Integer,nullable=False)
    divicion_curso = db.Column(db.String,nullable=False)


    def __repr__(self):
        return '<Alumno: {} -- DNI {} >'.format(self.nombre,self.dni)