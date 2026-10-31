# Checklist del Taller: Sistema de Gestión Académica (POO en Python) - Actividad N.1

## README.md
- [] Estructura de archivos
- [] Instrucciones para ejecutar el proyecto
- [] Explicacion breve de como se aplicaron la herencia, la sobre escritura y el polimosrfismo

## Fase 1: Modelado inicial del sistema (Clases base y constructores)
- [x] Crear la clase `persona`
    - Atributos: 
        - identificación
        - nombre
        - correo
    - Métodos `mostrar_informacion()`
- [x] Crear la clase `programaAcademico`
    - Atributos:
        - código
        - nombre
        - facultad
        - número de semestres
    - Métodos `mostrar_informacion()`
- [x] Crear la clase `asignatura`
    - Atributos:
        - código
        - nombre
        - número de créditos
        - programa académico
    - Métodos `mostrar_informacion()`
- [x] Configurar constructores (`__init__`) en todas las clases.

## Fase 2: Encapsulamiento y validación de datos
- [x] Aplicar encapsulamiento (atributos privados con `_` o `__`).
- [x] Implementar métodos getters y setters con validaciones:
  - [x] Correo electrónico no vacío.
  - [x] Número de semestres > 0.
  - [x] Número de créditos > 0.
- [x] Mensajes de advertencia cuando el valor ingresado sea inválido.

## Fase 3: Herencia (Especialización de personas)
- [x] Crear clase `estudiante` heredando de `persona`
    - Atributos extra:
        - código estudiantil
        - programa académico
        - semestre
        - promedio acumulado
- [x] Crear clase `docente` heredando de `persona`
    - Atributos extra:
        - número de empleado
        - facultad
        - tipo de contratación
        - horas semanales
- [x] Crear clase `administrativo` heredando de `persona`
    - Atributos extra:
        - número de empleado
        - dependencia
        - cargo
        - jornada
- [x] Utilizar `super()` en los constructores para reutilizar los atributos comunes.

## Fase 4: Sobrescritura de métodos (Polimorfismo estático / comportamientos particulares)
- [x] Sobrescribir `mostrar_informacion()` en `estudiante`, `docente` y `administrativo` para incluir sus datos específicos.
- [x] Implementar y sobrescribir el método `realizar_actividad_principal()` en cada clase hija con su comportamiento particular.

## Fase 5: Procesamiento conjunto y Polimorfismo dinámico
- [x] Crear una única colección (lista) en el programa principal con al menos 2 estudiantes, 2 docentes y 2 administrativos.
- [x] Recorrer la colección usando un **único ciclo** sin condicionales de tipo (`isinstance` o `type`), invocando `mostrar_informacion()` y `realizar_actividad_principal()`.

## Fase 6: Pruebas, Repositorio y Documentación (GitHub)
- [x] Escribir el script de pruebas en el archivo principal (`main.py`) cubriendo todos los requerimientos
    - [x] La creación de programas académicos y asignaturas.
    - [x] La creación de al menos seis personas.
    - [x] La consulta de la información de los objetos.
    - [x] La modificación válida de datos encapsulados.
    - [x] El intento de asignar al menos tres valores inválidos.
    - [x] La presentación particular de cada tipo de persona.
    - [x] El recorrido polimórfico de la colección de personas.


# Checklist del Taller: Sistema de Gestión Académica (POO en Python) - Actividad N.2

# Checklist del Taller: Evolución del Sistema de Gestión Académica (Actividad N°2)

## Fase 1: Generalización de las personas (Clases abstractas)
- [x] Importar `ABC` y `abstractmethod` del módulo `abc` en el archivo de modelos.
- [x] Modificar la clase `persona` para que herede de `ABC`.
- [x] Convertir el método `realizar_actividad_principal()` en un método abstracto usando el decorador `@abstractmethod`.
- [x] Verificar que Python impida la creación directa de objetos de la clase `persona` (lanzando `TypeError`).
- [x] Asegurar que las clases hijas (`Estudiante`, `Docente`, `Administrativo`) mantengan su implementación de `realizar_actividad_principal()`.

## Fase 2: Organización de la oferta académica (Composición y Grupos)
- [x] Crear la clase `Horario` con atributos: `dia`, `hora_inicio`, `hora_fin`, `salon` y su respectivo método para mostrar información.
- [x] Crear la clase `GrupoAcademico` con atributos: `codigo`, `asignatura` (objeto de tipo `Asignatura`), `docente` (objeto de tipo `Docente`), `capacidad_maxima`, `estudiantes_matriculados` (lista) y `horario` (objeto de tipo `Horario`).
- [x] Implementar los métodos obligatorios en `GrupoAcademico`:
  - [x] `mostrar_informacion_grupo()`
  - [x] `matricular_estudiante(estudiante)`
  - [x] `retirar_estudiante(codigo_estudiantil)`
  - [x] `mostrar_estudiantes()`
- [x] Validar que el grupo reciba objetos reales de `Asignatura`, `Docente` y `Horario`, y no textos sueltos.

## Fase 3: Relación de composición
- [x] Verificar que la clase `Horario` se instancie e integre dentro de la estructura de `GrupoAcademico` evidenciando composición (ciclo de vida ligado o dependencia estricta).
- [ ] Documentar en el archivo `README.md` y en el Documento de Decisiones de Diseño la justificación de por qué la relación entre grupo y horario es de composición y no de herencia.

## Fase 4: Control de situaciones excepcionales (Excepciones personalizadas)
- [ ] Crear clases de excepciones personalizadas heredando de `Exception`:
  - [ ] `EstudianteYaMatriculadoException`
  - [ ] `CapacidadMaximaExcedidaException`
  - [ ] `EstudianteNoMatriculadoException`
  - [ ] `AsignaturaNoExisteException`
  - [ ] `ProgramNoExisteException` (o similar para programa académico)
- [ ] Lanzar (`raise`) estas excepciones desde los métodos correspondientes del controlador o clases cuando ocurra la anomalía.
- [ ] Capturar (`try-except`) las excepciones en el programa principal (`main.py`) mostrando mensajes comprensibles y permitiendo que el flujo del programa continúe sin cerrarse bruscamente.

## Fase 5: Pruebas mínimas y Actualización de Controladores
- [x] Actualizar el controlador para administrar listas de horarios y grupos académicos.
- [x] Ampliar el menú interactivo con opciones para:
  - [x] Crear horarios y grupos académicos vinculando objetos existentes.
  - [x] Matricular estudiantes en un grupo.
  - [x] Retirar estudiantes de un grupo.
  - [ ] Buscar asignaturas y programas académicos (disparando las excepciones si no se encuentran).
- [ ] Implementar pruebas en el menú que demuestren:
  - [ ] Imposibilidad de instanciar `persona` directamente.
  - [ ] Matrícula correcta y rechazo de duplicados.
  - [ ] Control de capacidad máxima del grupo.
  - [ ] Retiro correcto y rechazo de estudiantes no matriculados.
  - [ ] Búsquedas fallidas controladas con excepciones personalizadas.

## Fase 6: Documentación y Entregables en Git (GitHub)
- [ ] Crear la etiqueta (tag) en Git denominada `Entrega_AC2`.
- [ ] Actualizar el archivo `README.md` con la información solicitada en la actividad (declaración de IA, estructura, etc.).
- [ ] Elaborar y adjuntar el **Documento de Decisiones de Diseño** en formato PDF o Markdown respondiendo detalladamente a todas las preguntas planteadas en la guía.
- [ ] Verificar que todos los integrantes del equipo cuenten con al menos un commit válido y registrado en el repositorio.