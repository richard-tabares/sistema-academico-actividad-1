class asignatura:
    def __init__(self, codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma):
        self.set_codigoAsignatura(codigoAsignatura)
        self.set_nombre(nombre)
        self.set_numeroDeCreditos(numeroDeCreditos)
        self.set_codigoPrograma(codigoPrograma)
        
    def mostrar_informacion(self):
        print(f"Codigo de la asignatura: {self.get_codigoAsignatura()}")
        print(f"Nombre de la asignatura: {self.get_nombre()}")
        print(f"Numeros de creditos: {self.get_numeroDeCreditos()}")
        print(f"Codigo del programa: {self.get_codigoPrograma()}")
    
    # Getters and Setters
    def set_codigoAsignatura(self, codigoAsignatura):
        self._codigoAsignatura = codigoAsignatura
        
    def get_codigoAsignatura(self):
        return self._codigoAsignatura
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_nombre(self):
        return self._nombre

    # Validación para que el número de créditos sea mayor que cero
    def set_numeroDeCreditos(self, numeroDeCreditos):
        if(numeroDeCreditos > 0):
            self._numeroDeCreditos = numeroDeCreditos
        else:
            raise ValueError("El número de créditos de la Asignatura debe ser mayor que cero")
        
    def get_numeroDeCreditos(self):
        return self._numeroDeCreditos
    
    def set_codigoPrograma(self, codigoPrograma):
        self._codigoPrograma = codigoPrograma
        
    def get_codigoPrograma(self):
        return self._codigoPrograma