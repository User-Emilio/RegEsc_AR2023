from ..services.service_alumnos import getDataAlumno

def Alumno(current_user):

    return getDataAlumno(current_user)