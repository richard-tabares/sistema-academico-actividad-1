from abc import ABC, abstractmethod

class persona(ABC):
    def __init__(self, nombre, identificacion, correo):
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_correo(correo)
        
    @abstractmethod
    def mostrar_informacion(self):
        print(f"Nombre de la persona: {self.get_nombre()}")
        print(f"Identificación: {self.get_identificacion()}")
        print(f"Correo Electronico: {self.get_correo()}")

    # Getters and Setters
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre
    
    def set_identificacion(self, identificacion):
        self._identificacion = identificacion

    def get_identificacion(self):
        return self._identificacion

    # Validación para que el correo electrónico no se reemplace por una cadena vacia
    def set_correo(self, correo):
        if correo.strip() == "":
            raise ValueError("El correo electrónico no puede estar vacio")
        self._correo = correo

    def get_correo(self):
        return self._correo
    