from models.programaAcademico import programaAcademico
from models.excepciones import ProgramaNoEncontradoExcepcion

TILDES = str.maketrans("áéíóúü", "aeiouu")

class programaController():

    def __init__(self):
        self.programas = []

    def agregar_programa(self, codigoPrograma, nombre, facultad, numeroDeSemestres):
        prog = programaAcademico(codigoPrograma, nombre, facultad, numeroDeSemestres)
        self.programas.append(prog)

    def get_programas(self):
        return self.programas.copy()
    
    def buscar_programa_por_nombre(self, nombre):
        programas_encontrados = [
            prog for prog in self.programas 
            if prog.get_nombre().lower().translate(TILDES) == nombre.lower().translate(TILDES)
            ]
        if not programas_encontrados:
            raise ProgramaNoEncontradoExcepcion(nombre) 
        return programas_encontrados
    
    