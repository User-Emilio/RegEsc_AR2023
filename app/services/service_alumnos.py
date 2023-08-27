from ..models.alumnos import Alumno

def getDataAlumno(current_user):

    alumno = Alumno.query.filter_by(dni=str(current_user.dni)).first()

    return alumno