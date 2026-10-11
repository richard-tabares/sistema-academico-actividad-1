class asignatura:
    def __init__(self, codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma):
        self.set_codigoAsignatura(codigoAsignatura)
        self.set_nombre(nombre)
        self.set_numeroDeCreditos(numeroDeCreditos)
        self.set_codigoPrograma(codigoPrograma)
        
    def mostrar_informacion(self):
        return self.get_codigoAsignatura(), self.get_nombre(), self.get_numeroDeCreditos(), self.get_codigoPrograma()
    
    # Getters and Setters
    def set_codigoAsignatura(self, codigoAsignatura):
        self._codigoAsignatura = codigoAsignatura
        
    def get_codigoAsignatura(self):
        return self._codigoAsignatura
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_nombre(self):
        return self._nombre
    
    def set_numeroDeCreditos(self, numeroDeCreditos):
        self._numeroDeCreditos = numeroDeCreditos
        
    def get_numeroDeCreditos(self):
        return self._numeroDeCreditos
    
    def set_codigoPrograma(self, codigoPrograma):
        self._codigoPrograma = codigoPrograma
        
    def get_codigoPrograma(self):
        return self._codigoPrograma