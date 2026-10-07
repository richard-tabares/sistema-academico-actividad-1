#Clase: Programa Academico
class programaAcademico:
    def __init__(self, codigoPrograma, nombre, facultad, numeroDeSemestres):
        self._codigoPrograma = codigoPrograma
        self._nombre = nombre
        self._facultad = facultad
        self._numeroDeSemestres = numeroDeSemestres

    # Método para mostrar la información del Programa Academico
    def mostrar_informacion(self):
        return self.get_codigoPrograma(), self.get_nombre(), self.get_facultad(), self.get_numeroDeSemestres()

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

    
