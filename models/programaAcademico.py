#Clase: Programa Academico
class programaAcademico:
    def __init__(self, codigoPrograma, nombre, facultad, numeroDeSemestres):
        self.codigoPrograma = codigoPrograma
        self.nombre = nombre
        self.facultad = facultad
        self.numeroDeSemestres = numeroDeSemestres

    # Método para mostrar la información del Programa Academico
    def mostrar_informacion(self):
        return f"Código de programa: {self.codigoPrograma}, Nombre: {self.nombre}, Facultad: {self.facultad}, Número de semestres: {self.numeroDeSemestres}"