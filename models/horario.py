class horario:
    def __init__(self, codigoHorario, dia, horaInicio, horaFinal, salon):
        self.set_codigoHorario(codigoHorario)
        self.set_dia(dia)
        self.set_horaInicio(horaInicio)
        self.set_horaFinal(horaFinal)
        self.set_salon(salon)

    def mostrar_informacion(self):
        print(f"Dia: {self.get_dia()} - Horario: {self.get_horaInicio()} a {self.get_horaFinal()} - Salon: {self.get_salon()}")

    # Getters and Setters
    def set_codigoHorario(self, codigoHorario):
        self._codigoHorario = codigoHorario

    def get_codigoHorario(self):
        return self._codigoHorario

    def set_dia(self, dia):
        self._dia = dia

    def get_dia(self):
        return self._dia

    def set_horaInicio(self, horaInicio):
        self._horaInicio = horaInicio

    def get_horaInicio(self):
        return self._horaInicio

    def set_horaFinal(self, horaFinal):
        self._horaFinal = horaFinal

    def get_horaFinal(self):
        return self._horaFinal

    def set_salon(self, salon):
        self._salon = salon

    def get_salon(self):
        return self._salon