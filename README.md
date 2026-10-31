# Sistema Académico

## Nombre de los integrantes
- Diana Paola Quintero Ceballos
- Richard Tabares Botero
- Roger Avila Uribe
- Laura Camila Parra Beltran

## Descripción general del proyecto
Primera versión de un Sistema de Gestión Académica en Python, que representa a una universidad, su personal, estudiantes, sus programas académicos y las asignaturas curriculares. Este sistema se basa en programación orientada a objetos, donde se evidencia la aplicación de clases, atributos, métodos, constructores, encapsulamiento, herencia, sobre escritura y polimorfismo.

## Estructura de los archivos
sistema-academico-actividad-1/
├── main.py                      # Menú interactivo y reporte polimórfico de personas
├── README.md
├── TASK.md                      # Lista de verificación de las fases del taller
├── controllers/
│   └── user_controller.py       # Controlador: crea y almacena las personas en una lista
│   └── programa_controller.py       # Controlador: crea y almacena los programas en una lista
│   └── asignatura_controller.py       # Controlador: crea y almacena las asignaturas en una lista
└── models/
    ├── persona.py               # Clase base con los datos comunes (nombre, identificación, correo)
    ├── estudiante.py            # Hereda de persona: código, programa académico, semestre y promedio
    ├── docente.py               # Hereda de persona: n.º de empleado, facultad, contratación y horas semanales
    ├── administrativo.py        # Hereda de persona: n.º de empleado, dependencia, cargo y jornada
    ├── programaAcademico.py     # Código, nombre, facultad y número de semestres
    └── asignatura.py            # Código, nombre, número de créditos y código del programa

## Instrucciones para ejecutar el proyecto
1. Tener instalado **Python 3.10 o superior**. No se requieren librerías externas.
2. Clonar o descargar el repositorio.
3. Ubicarse en la carpeta raíz del proyecto, donde está `main.py`:
   ```
   cd sistema-academico-actividad-1
   ```
4. Ejecutar:
   ```
   python main.py
   ```
   (en algunos sistemas el comando es `python3 main.py`).

Al iniciar, el sistema precarga seis personas (dos estudiantes, dos docentes y dos administrativos) y muestra un menú:

==================================================
    SISTEMA DE GESTIÓN ACADÉMICA - MENÚ PRINCIPAL
==================================================
*** Validaciones básicas *** 
*El correo del usuario no puede ir vacios
*El numero de semestres para el programar academico debe ser mayor a 0
*El numero de creditos para asignatura debe ser mayor a 0
**********************************************
1. Registrar Programa Académico
2. Registrar Asignatura
3. Registrar Estudiante
4. Registrar Docente
5. Registrar Personal Administrativo
6. Listar Programas
7. Listar Asignaturas
8. Generar Reporte Polimórfico de personas
9. Salir
Ingrese una opción del 1 al 9: 

## Explicación breve de cómo se aplicaron la herencia, la sobre escritura y el polimorfismo
**Encapsulamiento y validaciones.** Los atributos de todas las clases son privados por convención (`_atributo`) y se consultan o modifican mediante getters y setters. Los setters validan los datos: el correo no puede ser una cadena vacía, y el número de semestres de un programa y el de créditos de una asignatura deben ser mayores que cero. Cuando el valor no cumple, se lanza un `ValueError` con un mensaje claro, que `main.py` captura y muestra al usuario.

**Herencia.** La clase `persona` reúne lo que es común a todas las personas: nombre, identificación y correo. Las clases `estudiante`, `docente` y `administrativo` heredan de ella y solo agregan sus atributos particulares, de modo que los datos comunes no se repiten. El constructor de cada subclase llama a `super().__init__()` para inicializar la parte heredada.

**Sobre escritura.** Las tres subclases redefinen `mostrar_informacion()`. Cada una imprime su encabezado, llama a `super().mostrar_informacion()` para mostrar los datos generales de `persona` y luego agrega los datos propios (por ejemplo, el código y el promedio del estudiante, o la dependencia y la jornada del administrativo). Además, cada subclase implementa `realizar_actividad_principal()` con su propio comportamiento: el estudiante indica qué programa cursa y en qué semestre está, el docente en qué facultad orienta clases y el administrativo qué cargo desempeña y en qué dependencia.

**Polimorfismo.** El controlador (`userController`) guarda en una única lista, `personas`, objetos de los tres tipos. La función `mostrar_usuarios()` de `main.py` recorre esa lista con un solo ciclo `for` y, para cada elemento, invoca `mostrar_informacion()` y `realizar_actividad_principal()`. No usa condicionales ni distingue el tipo de objeto: Python ejecuta automáticamente la versión que corresponde a la clase real de cada uno, de manera que las mismas dos llamadas producen resultados distintos según se trate de un estudiante, un docente o un administrativo.
