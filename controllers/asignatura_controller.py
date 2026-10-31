from models.asignatura import asignatura
from models.excepciones import AsignaturaNoEncontradaExcepcion

TILDES = str.maketrans("áéíóúü", "aeiouu")

class asignaturaController():

    def __init__(self):
        self.asignaturas = []

    def agregar_asignatura(self, codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma):
        asig = asignatura(codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma)
        self.asignaturas.append(asig)

    def get_asignaturas(self):
        return self.asignaturas.copy()
    
    def buscar_asignatura_por_nombre(self, nombre):
        asignaturas_encontradas = [
            asig for asig in self.asignaturas 
            if asig.get_nombre().lower().translate(TILDES) == nombre.lower().translate(TILDES)
            ]
        if not asignaturas_encontradas:
            raise AsignaturaNoEncontradaExcepcion(nombre)
        return asignaturas_encontradas

    
    
