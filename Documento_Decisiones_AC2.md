# Documento de Decisiones de Diseño

## Sistema de Gestión Académica

### Actividad N.° 2 — Evolución del sistema

**Integrantes**

Richard Tabares Botero  
Roger Avila Uribe  
Laura Camila Parra Beltran

**Curso:** Programación 1  
**Docente:** Natalia Castellanos
**Universidad:** Universidad de Manizales  
**Facultad / Programa:** Ingeniería en Seguridad de la Información
**Fecha:** 31 de octubre de 2026


## 1. Introducción

El presente documento expone y justifica las principales decisiones de diseño adoptadas en la segunda versión del Sistema de Gestión Académica. La Actividad 1 estableció una jerarquía de personas, aplicó encapsulamiento, herencia, sobrescritura y polimorfismo; la Actividad 2 amplía ese modelo con una clase abstracta, grupos académicos, horarios, relaciones de composición y excepciones personalizadas. El objetivo no es describir el sistema función por función, sino explicar por qué la solución quedó organizada de la manera en que está y cómo cada decisión se refleja en el código.

La revisión se realizó sobre los tres componentes del proyecto: el modelo de dominio ubicado en `models/`, los controladores de `controllers/` y el menú principal de `main.py`. En cada apartado se citan las clases, los métodos y las líneas relevantes, de modo que las afirmaciones puedan verificarse directamente en la implementación. También se distinguen las decisiones propias de la jerarquía de personas, las relaciones entre entidades académicas, el tratamiento de errores y la conservación del polimorfismo construido en la actividad anterior.

## 2. Descripción general de la solución

### 2.1 Arquitectura y organización

El sistema se organiza en tres capas con responsabilidades diferenciadas. El modelo contiene las entidades del dominio y sus reglas básicas; los controladores administran colecciones de objetos y sirven de intermediarios; el menú principal captura datos, presenta información y coordina las operaciones. Esta separación evita que la lógica de almacenamiento quede mezclada con la interfaz de consola y facilita reutilizar el modelo en otra forma de presentación.

| Capa | Archivos principales | Responsabilidad |
|---|---|---|
| Modelo de dominio | `models/` | Representar las entidades, encapsular sus datos, validar reglas y definir las excepciones del dominio. |
| Controladores | `controllers/` | Crear objetos, almacenarlos en listas, buscarlos y delegar operaciones como matricular o retirar estudiantes. |
| Interfaz y coordinación | `main.py` | Precargar datos, mostrar el menú, solicitar información, invocar a los controladores y capturar los errores para continuar la ejecución. |

### 2.2 Clases del sistema

La jerarquía de personas se apoya en `persona`, que concentra nombre, identificación y correo. Las clases `estudiante`, `docente` y `administrativo` heredan de ella y agregan los datos propios de cada rol. Las entidades académicas son independientes de esa jerarquía: `programaAcademico`, `asignatura` y `horario` describen la oferta y la programación; `grupoAcademico` articula una asignatura, un docente, un horario y un conjunto de estudiantes matriculados.

| Clase | Papel dentro de la solución |
|---|---|
| `persona` | Clase abstracta con los datos comunes y el contrato de presentación de información. |
| `estudiante`, `docente`, `administrativo` | Especializaciones de `persona` con atributos, presentación y actividad principal propia. |
| `programaAcademico` | Programa al que pertenecen las asignaturas; valida que el número de semestres sea positivo. |
| `asignatura` | Unidad curricular con código, créditos y código del programa; valida los créditos. |
| `horario` | Día, hora de inicio, hora final y salón de una sesión. |
| `grupoAcademico` | Reúne asignatura, docente, capacidad, horario y estudiantes matriculados. |
| `SistemaAcademicoError` y derivadas | Excepciones de dominio con mensajes y datos de contexto. |
| Controladores | Repositorios en memoria que administran personas, programas, asignaturas, horarios y grupos. |

### 2.3 Flujo general de ejecución

`main()` crea una instancia de cada controlador y precarga seis personas, un programa, una asignatura y un horario (`main.py:100-108`). Después presenta un menú de opciones que permite registrar entidades, crear grupos, matricular o retirar estudiantes, listar información, buscar por nombre y generar el reporte polimórfico. Cada opción captura los datos y delega la creación o la operación en el controlador correspondiente; los errores de validación y las excepciones de dominio se atienden con `try/except` para que el menú continúe funcionando.

El flujo de matrícula ilustra la coordinación entre capas: el menú selecciona un estudiante y un grupo, el controlador localiza el grupo y este último aplica las reglas de duplicidad y capacidad. Si una regla se incumple, el modelo lanza una excepción personalizada que el menú captura y muestra al usuario. Así, la interfaz no duplica las validaciones y el modelo conserva la autoridad sobre sus propias invariantes.

## 3. Desarrollo

### 3.1 La abstracción de `persona`

La clase `persona` se implementó como clase abstracta porque en el dominio del sistema no existe una persona genérica que pueda registrarse por sí sola: los actores reales son estudiantes, docentes o administrativos, y cada uno posee datos y comportamientos que no se pueden reducir a los atributos comunes. Permitir la creación de una `persona` produciría un objeto incompleto, sin rol, sin actividad principal y sin la información específica que el resto del sistema espera. La abstracción evita esa situación y obliga a que todo objeto concreto pertenezca a una especialización válida.

En el código, la decisión se materializa al heredar de `ABC` y decorar `mostrar_informacion()` con `@abstractmethod` (`models/persona.py:1-13`). Gracias a ello, Python impide instanciar `persona` directamente y también impide instanciar una subclase que no implemente el método.

La clase abstracta también concentra la parte estable de la jerarquía: el constructor, los getters y setters, y la validación del correo electrónico (`models/persona.py:29-32`). Las subclases reutilizan esa lógica mediante `super().__init__()`, de modo que una regla como “el correo no puede estar vacío” se aplica a todas las personas sin repetirla. El método abstracto conserva además una implementación base que imprime los datos comunes; las subclases la invocan con `super().mostrar_informacion()` y luego agregan lo propio, siguiendo un patrón plantilla.

```python
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
```

### 3.2 Implementación del método abstracto y comportamiento de las derivadas

Las tres clases derivadas implementan `mostrar_informacion()` y cumplen el contrato de manera especializada. Cada una imprime un encabezado propio, llama a la implementación de `persona` para no duplicar los datos comunes y luego presenta sus atributos particulares. La existencia del método abstracto garantiza que el reporte polimórfico pueda invocarlo sobre cualquier objeto de la lista sin comprobar su tipo.

| Clase | Qué agrega `mostrar_informacion()` | Comportamiento de `realizar_actividad_principal()` | Atributos propios |
|---|---|---|---|
| `docente` | Número de empleado, facultad, tipo de contratación y horas semanales. | Indica que orienta clases en su facultad. | Datos laborales y académicos del docente. |
| `estudiante` | Código, programa académico, semestre y promedio. | Indica qué programa cursa y en qué semestre se encuentra. | Datos de identificación académica y rendimiento. |
| `administrativo` | Número de empleado, dependencia, cargo y jornada. | Indica el cargo que desempeña y la dependencia donde trabaja. | Datos laborales y de gestión. |

En `docente`, el método se define en `models/docente.py:12-18` y la actividad principal en `models/docente.py:20-21`; en `estudiante`, en `models/estudiante.py:12-18` y `models/estudiante.py:20-21`; en `administrativo`, en `models/administrativo.py:12-18` y `models/administrativo.py:20-21`. Las tres implementaciones respetan la misma firma, pero producen salidas distintas. Esa combinación de contrato común y resultado variable es precisamente lo que aporta el polimorfismo: el código cliente no necesita conocer la clase concreta para obtener la información correcta. El uso de `super()` en el constructor inicializa la parte heredada antes de asignar los atributos propios, y en `mostrar_informacion()` reutiliza la presentación común, de modo que un cambio futuro en `persona` no debe replicarse en tres archivos.

### 3.3 Relaciones entre Grupo Académico, Asignatura, Docente, Estudiante y Horario

Las relaciones se eligieron según el significado de cada vínculo. La herencia se reservó para la relación “es un” entre una persona y su rol. Las demás relaciones son de uso, referencia o pertenencia, por lo que se modelaron con asociaciones, agregación o composición. Forzar una jerarquía entre entidades que no son especializaciones de la misma cosa habría producido una estructura artificial.

```text
persona (ABC)
├── estudiante
├── docente
└── administrativo

grupoAcademico
├── asignatura                 → código de la asignatura
├── docente                    → número de empleado
├── horario                    → día, horas y salón (composición)
└── estudiantesMatriculados[]  → objetos estudiante (agregación)
```

| Relación | Tipo | Implementación en el código | Justificación |
|---|---|---|---|
| `persona` → `estudiante`, `docente`, `administrativo` | Herencia | `class estudiante(persona)`, `class docente(persona)`, `class administrativo(persona)` y `super().__init__()`. | Cada rol es una especialización de persona y comparte sus atributos y validaciones. |
| `grupoAcademico` → `asignatura` | Asociación dirigida por código | `set_asignatura()` guarda el resultado de `get_codigoAsignatura()` (`models/grupoAcademico.py:21-25`). | La asignatura existe de forma independiente en su controlador; el grupo solo necesita referenciarla. |
| `grupoAcademico` → `docente` | Asociación dirigida por código | `set_docente()` guarda el resultado de `getNumeroDeEmpleado()` (`models/grupoAcademico.py:27-31`). | El docente tiene vida propia y puede participar en varios grupos; el grupo conserva su identificador. |
| `grupoAcademico` → `estudiante` | Agregación | Lista `estudiantesMatriculados` con objetos `estudiante` y métodos `matricular_estudiante()` y `retirar_estudiante()` (`models/grupoAcademico.py:11,56-82`). | Los estudiantes existen fuera del grupo y pueden matricularse en otros; el grupo administra su matrícula. |
| `grupoAcademico` → `horario` | Composición / dependencia estricta | El constructor recibe un objeto `horario` y `set_horario()` integra sus datos (`models/grupoAcademico.py:6-12,42-46`). | El horario es parte constitutiva de la definición del grupo; sin él, el grupo no puede describirse académicamente. |
| `asignatura` → `programaAcademico` | Asociación por código | `set_codigoPrograma()` almacena el código del programa (`models/asignatura.py:37-41`). | La asignatura pertenece a un programa, pero ambos se gestionan como entidades independientes. |

El uso de identificadores para asignatura y docente reduce el acoplamiento y evita duplicar objetos completos dentro del grupo. La fuente de verdad sigue estando en los controladores, que conservan las listas de programas, asignaturas, docentes y grupos. Para los estudiantes se eligió una lista de objetos porque el grupo necesita consultar su código y su nombre al matricular, retirar y mostrar; esa referencia directa simplifica las operaciones sin romper la independencia del estudiante.

### 3.4 Composición entre Grupo Académico y Horario

La relación entre `grupoAcademico` y `horario` corresponde a composición y no a herencia porque un grupo académico no es un horario: un grupo es una oferta concreta de una asignatura con un docente, una capacidad y unos estudiantes; el horario describe cuándo y dónde se dicta esa oferta. La herencia solo tendría sentido si un grupo fuera una especialización de horario, lo cual es falso en el dominio.

La composición se apoya en la idea de “tiene un”. El grupo contiene un horario como parte de su definición y no puede construirse sin él. En el constructor de `grupoAcademico` se recibe un objeto `horario` y se invoca `set_horario()` (`models/grupoAcademico.py:6-12`); ese método utiliza los getters del horario para obtener día, hora de inicio, hora final y salón (`models/grupoAcademico.py:42-43`). La presentación del grupo vuelve a exponer esos datos en `mostrar_informacion_grupo()` (`models/grupoAcademico.py:48-54`). El vínculo es estructural: el horario forma parte de la información mínima con la que se identifica el grupo.

Si se hubiera usado herencia, el grupo habría quedado acoplado a la implementación completa de `horario`, incluyendo setters y getters que no necesita, y cualquier cambio en la clase base afectaría a todos los grupos. La composición, en cambio, permite que el grupo use solo los datos que requiere, mantiene separadas las responsabilidades y deja abierta la posibilidad de cambiar la forma de representar el horario sin alterar la identidad del grupo. En la implementación, el grupo conserva una representación textual construida a partir del objeto recibido, mientras que la clase `horario` sigue siendo la fuente de los datos; lo relevante es que la dependencia se declara explícitamente en el constructor y no mediante una herencia que no representa su naturaleza.

### 3.5 Excepciones personalizadas

El sistema distingue entre errores de validación y situaciones excepcionales del dominio. Los primeros se representan con `ValueError` y provienen de setters que rechazan datos inválidos: correo vacío en `persona.set_correo()` (`models/persona.py:29-32`), créditos menores o iguales a cero en `asignatura.set_numeroDeCreditos()` (`models/asignatura.py:28-32`) y semestres menores o iguales a cero en `programaAcademico.set_numeroDeSemestres()` (`models/programaAcademico.py:35-39`). Los segundos se representan con clases propias que heredan de `SistemaAcademicoError` (`models/excepciones.py:1-2`), lo que permite identificarlos, transportar datos de contexto y capturarlos de forma específica.

| Excepción | Situación que controla | Punto de generación | Manejo |
|---|---|---|---|
| `EstudianteYaMatriculadoExcepcion` | El estudiante ya pertenece al grupo. | `grupoAcademico.matricular_estudiante()` antes de agregar (`models/grupoAcademico.py:56-59`). | Se captura en la opción de matrícula de `main.py:357-360` y se muestra el mensaje. |
| `CapacidadMaximaExcedidaExcepcion` | El grupo alcanzó su capacidad máxima. | `grupoAcademico.matricular_estudiante()` cuando la lista está llena (`models/grupoAcademico.py:61-65`). | Se captura en el mismo flujo de matrícula y se informa al usuario. |
| `AsignaturaNoExisteExcepcion` | Se busca o se referencia una asignatura cuyo código no existe. | Métodos de búsqueda y validación de asignaturas en los controladores. | Permite informar el código faltante y continuar el menú. |
| `ProgramaNoExisteExcepcion` | Se busca o se referencia un programa académico inexistente. | Métodos de búsqueda y validación de programas en los controladores. | Permite informar el código faltante y continuar el menú. |
| `GrupoNoExisteExcepcion` | Se busca un grupo académico que no está registrado. | Búsqueda de grupos en `grupoAcademicoController`. | Permite rechazar la operación con un mensaje comprensible. |
| `SistemaAcademicoError` | Base común de las excepciones del dominio. | No se lanza directamente; agrupa a las anteriores. | Permite capturar cualquier error académico si no se necesita un tratamiento específico. |

Las excepciones de matrícula se lanzan desde el modelo porque allí viven las reglas que protegen la consistencia del grupo: no puede haber dos estudiantes con el mismo código ni más estudiantes que la capacidad. El controlador no duplica esas validaciones; solo localiza el grupo y delega. El menú captura las excepciones con `except (EstudianteYaMatriculadoExcepcion, CapacidadMaximaExcedidaExcepcion)` y muestra el texto generado, de modo que el usuario entiende el motivo y el programa no termina abruptamente. Las excepciones de búsqueda completan el esquema para las consultas por código y mantienen el mismo principio: el controlador informa qué recurso falta y el menú decide cómo presentarlo.

### 3.6 Continuidad del polimorfismo de la Actividad 1

El polimorfismo construido en la Actividad 1 se conserva porque la nueva versión mantiene una única colección de personas y un único recorrido para presentarlas. `userController` almacena estudiantes, docentes y administrativos en la lista `personas` (`controllers/user_controller.py:8-24`) y la entrega mediante una copia en `get_personas()`. `main.mostrar_usuarios()` recorre esa lista con un solo ciclo, sin `isinstance` ni condicionales de tipo, e invoca `mostrar_informacion()` y `realizar_actividad_principal()` sobre cada elemento (`main.py:9-20`).

```python
for usuario in usuarios:
    usuario.mostrar_informacion()
    print(f"Su actividad principal es: ", end="")
    usuario.realizar_actividad_principal()
    print("-" * 100)
```

La diferencia respecto de la actividad anterior es que ahora `persona` es abstracta. Esto refuerza el polimorfismo en lugar de reemplazarlo: cualquier objeto que llegue a la lista debe pertenecer a una subclase concreta y debe implementar el método abstracto. Por eso el ciclo puede confiar en que la llamada siempre tendrá una implementación válida. La abstracción convierte una expectativa implícita en una garantía del lenguaje.

Agregar un nuevo tipo de persona no exigiría modificar el reporte polimórfico. Bastaría con crear una clase que herede de `persona`, implemente `mostrar_informacion()` y su actividad principal, y agregarla a la lista del controlador. El ciclo de `mostrar_usuarios()` seguiría siendo el mismo y produciría la salida correcta para el nuevo rol, lo que manifiesta el principio de abierto para extensión y cerrado para modificación.

En el menú existen filtros con `type(p).__name__` para listar docentes o estudiantes en las operaciones de grupos (`main.py:246,323`). Esos filtros cumplen una función de selección de la interfaz y no intervienen en el reporte polimórfico: para elegir qué docente asignar a un grupo hace falta distinguir el tipo, pero para presentar a todas las personas no se necesita conocerlo. Las funciones de listado de asignaturas, horarios, programas y grupos también reutilizan `mostrar_informacion()` o `mostrar_informacion_grupo()`, lo que evidencia un uso consistente de interfaces comunes en todo el modelo.

## 4. Conclusiones

La decisión de convertir `persona` en una clase abstracta respondió a una necesidad del dominio y no solo a una exigencia académica. Al no existir una persona genérica, la abstracción impide objetos incompletos y garantiza que todo actor del sistema tenga un rol y una forma de presentar su información. La reutilización de validaciones y de la presentación común, junto con el uso de `super()`, reduce la duplicación y mantiene un punto único de cambio para los datos compartidos.

Las clases derivadas implementan el método abstracto con comportamientos diferenciados: el docente muestra su información laboral y su actividad de enseñanza, el estudiante sus datos académicos y su actividad de formación, y el administrativo sus datos de gestión y su función en la dependencia. El contrato común permite que un único ciclo trate a los tres tipos como personas, mientras cada uno conserva su identidad. Así, la Actividad 2 no reemplaza el polimorfismo de la Actividad 1, sino que lo fortalece con una base formal.

Las relaciones entre las entidades académicas se eligieron por su significado: herencia para la relación “es un”, asociación por código para asignatura, docente y programa, agregación para los estudiantes matriculados y composición para el horario. Esta distribución evita jerarquías artificiales y reduce el acoplamiento. Finalmente, las excepciones personalizadas y las validaciones con `ValueError` distinguen entre datos inválidos y reglas académicas incumplidas; el modelo lanza las excepciones, los controladores localizan las entidades y el menú las captura sin cerrar el programa. El resultado es una solución cohesionada, extensible y coherente con la programación orientada a objetos.

## 5. Referencias del proyecto

| Archivo | Contenido citado |
|---|---|
| `models/persona.py` | Clase abstracta, constructor, `mostrar_informacion()` abstracto y validación del correo. |
| `models/docente.py` | Implementación del método abstracto y actividad principal del docente. |
| `models/estudiante.py` | Implementación del método abstracto y actividad principal del estudiante. |
| `models/administrativo.py` | Implementación del método abstracto y actividad principal del administrativo. |
| `models/programaAcademico.py` | Validación del número de semestres. |
| `models/asignatura.py` | Validación de créditos y referencia al programa académico. |
| `models/horario.py` | Datos del horario y getters utilizados por el grupo. |
| `models/grupoAcademico.py` | Composición del horario, asociaciones, matrícula, retiro y listado de estudiantes. |
| `models/excepciones.py` | Jerarquía de excepciones del dominio académico. |
| `controllers/user_controller.py` | Lista heterogénea de personas y operaciones de registro. |
| `controllers/grupoAcademico_controller.py` | Búsqueda y administración de grupos académicos. |
| `main.py` | Menú, precarga, reporte polimórfico y manejo de excepciones. |
| `README.md` | Explicación general de herencia, sobrescritura, polimorfismo y composición. |

## 6. Declaración de uso de inteligencia artificial

Para la elaboración de este documento técnico nos apoyamos en herramientas de inteligencia artificial como apoyo para estudiar y comprender los conceptos de programación orientada a objetos y para la redacción y revisión del texto. Las decisiones de diseño, la implementación del sistema y la verificación de la información presentada fueron realizadas y validadas por los integrantes del equipo.
