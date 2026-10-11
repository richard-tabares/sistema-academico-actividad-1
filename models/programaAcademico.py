#Clase: Programa Academico
class programaAcademico:
    def __init__(self, codigoPrograma, nombre, facultad, numeroDeSemestres):
        self.set_codigoPrograma(codigoPrograma)
        self.set_nombre(nombre)
        self.set_facultad(facultad)
        self.set_numeroDeSemestres(numeroDeSemestres)

    def mostrar_informacion(self):
        return f"Código de programa: {self.get_codigoPrograma()}, Nombre: {self.get_nombre()}, Facultad: {self.get_facultad()}, Número de semestres: {self.get_numeroDeSemestres()}"

    # Getters and Setters
    def set_codigoPrograma(self, codigoPrograma):
        self._codigoPrograma = codigoPrograma

    def get_codigoPrograma(self):
        return self._codigoPrograma

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_facultad(self, facultad):
        self._facultad = facultad

    def get_facultad(self):
        return self._facultad

    def set_numeroDeSemestres(self, numeroDeSemestres):
        self._numeroDeSemestres = numeroDeSemestres

    def get_numeroDeSemestres(self):
        return self._numeroDeSemestres
    