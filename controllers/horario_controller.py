from models.horario import horario

class horarioController():
    
    def __init__(self):
        self.horarios = []

    def agregar_horario(self, codigoHorario, dia, horaInicio, horaFin, salon):
        nuevoHorario = horario(codigoHorario, dia, horaInicio, horaFin, salon)
        self.horarios.append(nuevoHorario)

    def get_horarios(self):
        return self.horarios.copy()