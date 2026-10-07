
#Importar Clases
from models.programaAcademico import programaAcademico
from models.persona import persona
from models.asignatura import asignatura

# Crear una instancia de la clase persona
person = persona("Roger", "10171550171", "roger@example.com")

# Crear una instancia de la clase Programa Academico
programa1 = programaAcademico("ISI001", "Ingeniería en Seguridad de la Información", "Facultad de Ingenierías", 9)

# Crear una instancia de la clase asignatura
asignature = asignatura("MAT001", "Matemáticas", 3, "PRO001")

# Mostrar la información de la persona
print(person.mostrar_informacion())

# Mostrar la información del Programa Academico
print(programa1.mostrar_informacion())

# Mostrar la información de la asignatura
print(asignature.mostrar_informacion())