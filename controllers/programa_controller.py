from models.programaAcademico import programaAcademico

class programaController():

    def __init__(self):
        self.programas = []

    def agregar_programa(self, codigoPrograma, nombre, facultad, numeroDeSemestres):
        prog = programaAcademico(codigoPrograma, nombre, facultad, numeroDeSemestres)
        self.programas.append(prog)

    def get_programas(self):
        return self.programas.copy()
    
    def buscar_programa_por_nombre(self, nombre):
        return [prog for prog in self.programas if prog.get_nombre() == nombre]
    