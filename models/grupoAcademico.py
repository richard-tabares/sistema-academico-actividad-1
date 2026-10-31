from models.horario import horario

from models.excepciones import EstudianteYaMatriculadoExcepcion, CapacidadMaximaExcedidaExcepcion

class grupoAcademico:
    def __init__(self, codigoGrupo, asignatura, docente, capacidad, horario):
        self.set_codigoGrupo(codigoGrupo)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad(capacidad)
        self.estudiantesMatriculados = []
        self.set_horario(horario)
          
    # Getters and Setters
    def set_codigoGrupo(self, codigoGrupo):
        self._codigoGrupo = codigoGrupo
        
    def get_codigoGrupo(self):
        return self._codigoGrupo

    def set_asignatura(self, asignatura):
        self._asignatura = asignatura.get_codigoAsignatura()

    def get_asignatura(self):
        return self._asignatura

    def set_docente(self, docente):
        self._docente = docente.getNumeroDeEmpleado()

    def get_docente(self):
        return self._docente

    def set_capacidad(self, capacidad):
        self._capacidad = capacidad

    def get_capacidad(self):
        return self._capacidad
    
    def get_estudiantes_matriculados(self):
        return self.estudiantesMatriculados.copy()

    def set_horario(self, horario):
        self._horario = (f"Dia: {horario.get_dia()} - Horario: {horario.get_horaInicio()} a {horario.get_horaFinal()} - Salon: {horario.get_salon()}")

    def get_horario(self):
        return self._horario

    def mostrar_informacion_grupo(self):
        print(f"Codigo del grupo: {self.get_codigoGrupo()}")
        print(f"Asignatura: {self.get_asignatura()}")
        print(f"Docente: {self.get_docente()}")
        print(f"Capacidad: {self.get_capacidad()}")
        self.mostrar_estudiantes()
        print(f"Horario: {self.get_horario()}")

    def matricular_estudiante(self, estudiante):
        for est in self.estudiantesMatriculados:
            if est.getCodigoEstudiante() == estudiante.getCodigoEstudiante():
                raise EstudianteYaMatriculadoExcepcion(estudiante.getCodigoEstudiante(), self.get_codigoGrupo())
            
        if len(self.estudiantesMatriculados) < self.get_capacidad():
            self.estudiantesMatriculados.append(estudiante)
            print(f"Estudiante matriculado en el grupo {self.get_codigoGrupo()}")
        else:
            raise CapacidadMaximaExcedidaExcepcion(self.get_codigoGrupo(), self.get_capacidad())
        print(f"Horario: {self.get_horario()}")  

    def retirar_estudiante(self, codigoEstudiante):
        for est in self.estudiantesMatriculados:
            if est.getCodigoEstudiante() == codigoEstudiante:
                self.estudiantesMatriculados.remove(est)
                print(f"Estudiante retirado del grupo {self.get_codigoGrupo()}")
                return
        print("El estudiante no está matriculado en este grupo.")

    def mostrar_estudiantes(self):
        if not self.estudiantesMatriculados:
            print(f"El grupo {self.get_codigoGrupo()} no tiene estudiantes matriculados.")
            return
        print(f"Estudiantes matriculados en el grupo {self.get_codigoGrupo()}:")
        for estudiante in self.estudiantesMatriculados:
            print(f" - Código: {estudiante.getCodigoEstudiante()} | Nombre: {estudiante.get_nombre()}")