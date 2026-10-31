from models.persona import persona

class docente (persona):

    def __init__(self, nombre, identificacion, correo, numeroDeEmpleado, facultad, tipoDeContratacion, numeroDeHorasSemanales):
        super().__init__(nombre, identificacion, correo)
        self.setNumeroDeEmpleado(numeroDeEmpleado)
        self.setFacultad(facultad)
        self.setTipoDeContratacion(tipoDeContratacion)
        self.setNumeroDeHorasSemanales(numeroDeHorasSemanales)

    def mostrar_informacion(self):
        print(f"---INFORMACION DOCENTE---")
        super().mostrar_informacion()
        print(f"Numero de empleado: {self.getNumeroDeEmpleado()}")
        print(f"Facultad: {self.getFacultad()}")
        print(f"Tipo de contratacion: {self.getTipoDeContratacion()}")
        print(f"Número de horas semanales: {self.getNumeroDeHorasSemanales()}")
    
    def realizar_actividad_principal(self):
        print(f"El docente {self.get_nombre()} orienta clases en la facultad de {self.getFacultad()}.")
        
    # SETTERS
    def setNumeroDeEmpleado(self, numeroDeEmpleado):
        self._numeroDeEmpleado = numeroDeEmpleado

    def setFacultad(self, facultad):
        self._facultad = facultad 

    def setTipoDeContratacion(self, tipoDeContratacion):
        self._tipoDeContratacion = tipoDeContratacion

    def setNumeroDeHorasSemanales(self, numeroDeHorasSemanales):
        self._numeroDeHorasSemanales = numeroDeHorasSemanales

    # GETTERS
    def getNumeroDeEmpleado(self):
        return self._numeroDeEmpleado

    def getFacultad(self):
        return self._facultad
    
    def getTipoDeContratacion(self):
        return self._tipoDeContratacion

    def getNumeroDeHorasSemanales(self):
        return self._numeroDeHorasSemanales
    