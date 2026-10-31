from models.persona import persona

class estudiante (persona):
    
    def __init__(self, nombre, identificacion, correo, codigoEstudiante, programaAcademico, semestre, promedio):
        super().__init__(nombre, identificacion, correo)
        self.setCodigoEstudiante(codigoEstudiante)
        self.setProgramaAcademico(programaAcademico)
        self.setSemestre(semestre)
        self.setPromedio(promedio)
    
    def mostrar_informacion(self):
        print(f"---INFORMACION ESTUDIANTE---")
        super().mostrar_informacion()
        print(f"Codigo del estudiante: {self.getCodigoEstudiante()}")
        print(f"Programa academico: {self.getProgramaAcademico()}")
        print(f"Semestre: {self.getSemestre()}")
        print(f"Promedio: {self.getPromedio()}")
    
    def realizar_actividad_principal(self):
        print(f"El estudiante {self.get_nombre()} cursa el programa {self.getProgramaAcademico()} y se encuentra en el semestre {self.getSemestre()}.")
        
    # SETTERs
    def setCodigoEstudiante(self, codigoEstudiante):
        # validaciones
        self._codigoEstudiante = codigoEstudiante
        
    def setProgramaAcademico(self, programaAcademico):
        self._programaAcademico = programaAcademico
    
    def setSemestre(self, semestre):
        self._semestre = semestre
        
    def setPromedio(self, promedio):
        self._promedio = promedio
        
    # GETTERS
    def getCodigoEstudiante(self):
        return self._codigoEstudiante
    
    def getProgramaAcademico(self):
        return self._programaAcademico

    def getSemestre(self):
        return self._semestre

    def getPromedio(self):
        return self._promedio