class SistemaAcademicoError(Exception):
    """Clase base de todas las situaciones excepcionales del dominio académico."""


# ---------------------------------------------------------------------------
# Excepciones del proceso de matrícula (se lanzan desde grupoAcademico)
# ---------------------------------------------------------------------------
class EstudianteYaMatriculadoExcepcion(SistemaAcademicoError):
    """El estudiante que se intenta matricular ya pertenece al grupo."""

    def __init__(self, codigoEstudiante, codigoGrupo):
        self.codigoEstudiante = codigoEstudiante
        self.codigoGrupo = codigoGrupo
        super().__init__(
            f"El estudiante {codigoEstudiante} ya está matriculado en el grupo {codigoGrupo}."
        )


class CapacidadMaximaExcedidaExcepcion(SistemaAcademicoError):
    """El grupo ya alcanzó su capacidad máxima y no admite más estudiantes."""

    def __init__(self, codigoGrupo, capacidad):
        self.codigoGrupo = codigoGrupo
        self.capacidad = capacidad
        super().__init__(
            f"El grupo {codigoGrupo} alcanzó su capacidad máxima ({capacidad} estudiantes)."
        )



# ---------------------------------------------------------------------------
# Excepciones de búsqueda (se lanzan desde los controladores)
# ---------------------------------------------------------------------------
class AsignaturaNoExisteExcepcion(SistemaAcademicoError):
    """No existe una asignatura registrada con el código buscado."""

    def __init__(self, codigoAsignatura):
        self.codigoAsignatura = codigoAsignatura
        super().__init__(
            f"No existe una asignatura registrada con el código '{codigoAsignatura}'."
        )


class ProgramaNoExisteExcepcion(SistemaAcademicoError):
    """No existe un programa académico registrado con el código buscado."""

    def __init__(self, codigoPrograma):
        self.codigoPrograma = codigoPrograma
        super().__init__(
            f"No existe un programa académico registrado con el código '{codigoPrograma}'."
        )


class GrupoNoExisteExcepcion(SistemaAcademicoError):
    """No existe un grupo académico registrado con el código buscado."""

    def __init__(self, codigoGrupo):
        self.codigoGrupo = codigoGrupo
        super().__init__(
            f"No existe un grupo académico registrado con el código '{codigoGrupo}'."
        )
