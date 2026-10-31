from models.asignatura import asignatura

class asignaturaController():

    def __init__(self):
        self.asignaturas = []

    def agregar_asignatura(self, codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma):
        asig = asignatura(codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma)
        self.asignaturas.append(asig)

    def get_asignaturas(self):
        return self.asignaturas.copy()
    
    def buscar_asignatura_por_nombre(self, nombre):
        return [asig for asig in self.asignaturas if asig.get_nombre() == nombre]
