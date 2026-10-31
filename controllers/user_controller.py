from models.estudiante import estudiante
from models.docente import docente
from models.administrativo import administrativo

class userController():
    
    def __init__(self):
        self.personas = []
        
    def agregar_estudiante(self, nombre, identificacion, correo, codigoEstudiante, programaAcademico, semestre, promedio):
        estu = estudiante(nombre, identificacion, correo, codigoEstudiante, programaAcademico, semestre, promedio)
        self.personas.append(estu)
        return estu
        
    def agregar_docente(self, nombre, identificacion, correo, numeroDeEmpleado, facultad, tipoDeContratacion, numeroDeHorasSemanales):
        doce = docente(nombre, identificacion, correo, numeroDeEmpleado, facultad, tipoDeContratacion, numeroDeHorasSemanales)
        self.personas.append(doce)
        
    def agregar_administrativo(self, nombre, identificacion, correo, numeroDeEmpleado, dependencia, cargo, jornada):
        admin = administrativo(nombre, identificacion, correo, numeroDeEmpleado, dependencia, cargo, jornada)
        self.personas.append(admin)
        
    def get_personas(self):
        return self.personas.copy()