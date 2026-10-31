from models.persona import persona 

class administrativo (persona):

    def __init__(self, nombre, identificacion, correo, numeroDeEmpleado, dependencia, cargo, jornada):
        super().__init__(nombre, identificacion, correo)
        self.setNumeroDeEmpleado(numeroDeEmpleado)
        self.setDependencia(dependencia)
        self.setCargo(cargo)
        self.setJornada(jornada)

    def mostrar_informacion(self):
        print(f"---INFORMACION ADMINISTRATIVO---")
        super().mostrar_informacion()
        print(f"Numero de empleado: {self.getNumeroDeEmpleado()}")
        print(f"Dependencia: {self.getDependencia()}")
        print(f"Cargo: {self.getCargo()}")
        print(f"Jornada: {self.getJornada()}")
    
    def realizar_actividad_principal(self):
        print(f"El administrativo {self.get_nombre()} desempeña el cargo de {self.getCargo()} en la dependencia de {self.getDependencia()}.")

    # SETTERS
    def setNumeroDeEmpleado(self, numerodeEmpleado):
        self._numeroDeEmpleado = numerodeEmpleado

    def setDependencia(self, dependencia):
        self._dependencia = dependencia

    def setCargo(self, cargo):
        self._cargo = cargo

    def setJornada(self, jornada):
        self._jornada = jornada

    # GETTERS
    def getNumeroDeEmpleado(self):
        return self._numeroDeEmpleado

    def getDependencia(self):
        return self._dependencia

    def getCargo(self):
        return self._cargo 

    def getJornada(self):
        return self._jornada

    
