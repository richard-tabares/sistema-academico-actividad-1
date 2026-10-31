from models.grupoAcademico import grupoAcademico

class grupoAcademicoController():

    def __init__(self):
        self.gruposAcademicos = []

    def agregar_grupo_academico(self, codigoGrupo, asignatura, docente, capacidad, horario):
        grupo = grupoAcademico(codigoGrupo, asignatura, docente, capacidad, horario)
        self.gruposAcademicos.append(grupo)
        
    def agregar_estudiante(self, codigoGrupo, estudiante):
        grupo = self.buscar_grupo_academico(codigoGrupo)
        if grupo is None:
            print(f"No existe un grupo academico con ese codigo")
            return
        grupo.matricular_estudiante(estudiante)
    
    def retirar_estudiante(self, codigoGrupo, codigoEstudiante):
        grupo = self.buscar_grupo_academico(codigoGrupo)
        if grupo is None:
            print(f"No existe un grupo academico con ese codigo")
            return
        grupo.retirar_estudiante(codigoEstudiante)

    def buscar_grupo_academico(self, codigoGrupo):
        for grupo in self.gruposAcademicos:
            if grupo.get_codigoGrupo() == codigoGrupo:
                return grupo
        return None
    
    def get_grupos_academicos(self):
        return self.gruposAcademicos.copy()