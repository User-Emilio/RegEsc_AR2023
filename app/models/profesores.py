from . import db

class Profesor(db.Model):
    
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    apellido = db.Column(db.String,nullable=False)
    
    def __repr__(self):
        return "<Profesor: {},{} >".format(self.nombre,self.apellido)