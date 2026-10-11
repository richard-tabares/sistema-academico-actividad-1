class persona:
    def __init__(self, nombre, identificacion, correo):
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_correo(correo)

    def mostrar_informacion(self):
        return self.get_nombre(), self.get_identificacion(), self.get_correo()

    # Getters and Setters
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre
    
    def set_identificacion(self, identificacion):
        self._identificacion = identificacion

    def get_identificacion(self):
        return self._identificacion

    def set_correo(self, correo):
        self._correo = correo

    def get_correo(self):
        return self._correo
    