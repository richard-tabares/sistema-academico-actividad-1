#Clase: Programa Academico
class programaAcademico:
    def __init__(self, codigoPrograma, nombre, facultad, numeroDeSemestres):
        self.set_codigoPrograma(codigoPrograma)
        self.set_nombre(nombre)
        self.set_facultad(facultad)
        self.set_numeroDeSemestres(numeroDeSemestres)

    def mostrar_informacion(self):
        print(f"Codigo del programa: {self.get_codigoPrograma()}")
        print(f"Nombre del programa: {self.get_nombre()}")
        print(f"Nombre de la facultad: {self.get_facultad()}")
        print(f"Numero de semestres: {self.get_numeroDeSemestres()}")

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

    # Validación para que el número de semestres sea mayor que cero
    def set_numeroDeSemestres(self, numeroDeSemestres):
        if(numeroDeSemestres > 0):
            self._numeroDeSemestres = numeroDeSemestres
        else:
            raise ValueError("El número de semestres del Programa Académico debe ser mayor que cero")

    def get_numeroDeSemestres(self):
        return self._numeroDeSemestres
    