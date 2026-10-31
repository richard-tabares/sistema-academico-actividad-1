from controllers.user_controller import userController
from controllers.asignatura_controller import asignaturaController
from controllers.programa_controller import programaController
from controllers.horario_controller import horarioController
from controllers.grupoAcademico_controller import grupoAcademicoController
from models.excepciones import (EstudianteYaMatriculadoExcepcion, CapacidadMaximaExcedidaExcepcion)

# metodo para mostrar todo los usuario y aplica POLIMORFISMO
def mostrar_usuarios(user_controller):
    usuarios = user_controller.get_personas()
    
    if not usuarios:
        print("Sin personas para mostrar")
        return
    
    for usuario in usuarios:
        usuario.mostrar_informacion()
        print(f"Su actividad principal es: ", end="")
        usuario.realizar_actividad_principal()
        print("-"*100)

# metodo para mostrar todo las asignaturas
def mostrar_asignaturas(asignatura_controller):
    asignaturas = asignatura_controller.get_asignaturas()
    
    if not asignaturas:
        print("Sin asignaturas para mostrar")
        return
    
    for asignatura in asignaturas:
        asignatura.mostrar_informacion()
        print("-"*100)

# metodo para mostrar todos los programas
def mostrar_programas(programa_controller):
    programas = programa_controller.get_programas()
    
    if not programas:
        print("Sin programas para mostrar")
        return
    
    for programa in programas:
        programa.mostrar_informacion()
        print("-"*100)
        
# metodo para mostrar todos los grupos
def mostrar_grupos(grupo_academico_controller):
    grupos = grupo_academico_controller.get_grupos_academicos()
    
    if not grupos:
        print("Sin grupos academicos para mostrar")
        return
    
    for grupo in grupos:
        grupo.mostrar_informacion_grupo()
        print("-"*100)
        
# metodo para mostrar todos estudiantes matriculados
def mostrar_estudiantes_matriculados(grupo_academico_controller):
    gruposEstudiantes = grupo_academico_controller.get_grupos_academicos()
    
    if not gruposEstudiantes:
        print("Sin grupos academicos para mostrar")
        return
    
    for gruposEstudiante in gruposEstudiantes:
        gruposEstudiante.mostrar_estudiantes()
        print("-"*100)
        
# metodo para mostrar todos los horarios
def mostrar_horarios(horario_controller):
    horarios = horario_controller.get_horarios()
    
    if not horarios:
        print("Sin horarios para mostrar")
        return
    
    for horario in horarios:
        horario.mostrar_informacion()
        print("-"*100)

def main():
    
    # Inicializamos el controlador de usuarios
    user_controller = userController()

    # Inicializamos el controlador de asignaturas
    asignatura_controller = asignaturaController()

    # Inicializamos el controlador de programas
    programa_controller = programaController()
    
    # Inicializamos el controlador de horarios
    horario_controller = horarioController()
    
    # Inicializamos el controlador de grupos academicos
    grupo_academico_controller = grupoAcademicoController()
    
    # Precargamos algunos datos
    user_controller.agregar_estudiante("Lucía Pérez", "1010222", "lucia-perez@gmail.com", "EST-01", "Ingeniería de Sistemas", 3, 4.3)
    user_controller.agregar_estudiante("Mateo Gómez", "1010333", "mateo.gomez@um.edu.co", "EST-02", "Ingeniería de Sistemas", 1, 4.0)
    user_controller.agregar_docente("Dr. Alberto Rueda", "987654", "alberto.rueda@um.edu.co", "EMP-D-01", "Facultad de Ingeniería", "Planta", 40)
    user_controller.agregar_docente("Dra. Sofia Castro", "987655", "sofia.castro@um.edu.co", "EMP-D-02", "Facultad de Ciencias", "Cátedra", 16)
    user_controller.agregar_administrativo("Carla Mendoza", "554433", "carla.mendoza@um.edu.co", "EMP-A-01", "Registro Académico", "Coordinadora", "Completa")
    user_controller.agregar_administrativo("Julián Ruiz", "554434", "julian.ruiz@um.edu.co", "EMP-A-02", "Biblioteca", "Asistente", "Media")
    asignatura_controller.agregar_asignatura("PRO001", "Programación 1", 4, "ING001")
    programa_controller.agregar_programa("ING001", "Ingenieria en Seguridad de la Información", "Ingenierias", 9)
    horario_controller.agregar_horario("H001", "Lunes", "18:00", "20:00", "1")
    
    while True:
        
        print("\n")
        print("==================================================")
        print("    SISTEMA DE GESTIÓN ACADÉMICA - MENÚ PRINCIPAL")
        print("==================================================")
        print("===>   Se auto preacarga los siguientes datos   <===")
        print("+ 2 Usuarios Estudiantes")
        print("+ 2 Usuarios Docentes")
        print("+ 2 Usuarios Administrativos")
        print("+ 1 Progarma Académico")
        print("+ 1 Asignatura")
        print("+ 1 Horario")
        print("===> *** Validaciones básicas *** <===")
        print("*El correo del usuario no puede ir vacios")
        print("*El numero de semestres para el programar academico debe ser mayor a 0")
        print("*El numero de creditos para asignatura debe ser mayor a 0")
        print("="*50)
        print("\n")
        print("OPCIONES")
        print("1. Registrar Programa Académico")
        print("2. Registrar Asignatura")
        print("3. Registrar Estudiante")
        print("4. Registrar Docente")
        print("5. Registrar Personal Administrativo")
        print("6. Registrar Grupo Académico")
        print("7. Registrar Horario")
        print("8. Matricula Estudiante")
        print("9. Retirar Estudiante Estudiante")
        print("10. Listar Programas")
        print("11. Listar Asignaturas")
        print("12. Listar Grupo Academicos")
        print("13. Listar Horarios")
        print("14. Listar Estudiantes Matriculados")
        print("15. Generar Reporte Polimórfico de personas")
        print("16. Buscar asignaturas por nombre")
        print("17. Buscar programas por nombre")
        print("0. Salir")
        
        # capturamos la opcion a ejecutar
        option = input("Ingrese una opción del 1 al 15: ").strip()
        print("\n")
        
        # se optado por utiliza un try except para capturar los errores en cada una de los casos
        match option:
            
            case '1':
                print("\n--- Registrar Programa Academico ---")
                try:
                    # capturamos los datos del programa
                    codigoPrograma = input("Ingrese el codigo del programa: ")
                    nombre = input("Ingrese el nombre del programa: ")
                    facultad = input("Ingresa facultad a la que pertenece: ")
                    numeroDeSemestres = int(input("Ingrese el numero de semestres: "))
                                    
                    # utilizamos el controlador para agregar un nuevo programa
                    programa_controller.agregar_programa(
                        codigoPrograma, nombre, facultad, numeroDeSemestres)
                                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            case '2':
                print("\n--- Registrar Asignatura ---")
                try:
                    # capturamos los datos de la asignatura
                    codigoAsignatura = input("Ingrese el codigo de la asignatura: ")
                    nombre = input("Ingrese el nombre de la asignatura: ")
                    numeroDeCreditos = int(input("Ingresa numero de los creditos: "))
                    codigoPrograma = input("Ingrese el codigo del programa: ")
                                    
                    # utilizamos el controlador para agregar una nueva asignatura
                    asignatura_controller.agregar_asignatura(
                        codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma)
                                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            
            case '3':
                print("\n--- Registrar Estudiante ---")
                try:
                    # capturamos los datos del usuario estudiante
                    nombre = input("Ingrese nombre del estudiante: ")
                    identificacion = input("Ingrese identificacion del estudiantes: ")
                    correo = input("Ingresa correo electronico: ")
                    codigoEstudiante = input("Ingrese el codigo del estudiante: ")
                    programaAcademico = input("Ingrese programa academico: ")
                    semestre = input("Ingrese semestre que actualmente cursa: ")
                    promedio = input("Ingrese promedio: ")
                    
                    # utilizamos el controlador para agregar un nuevo estudiante
                    user_controller.agregar_estudiante(nombre, identificacion, correo, codigoEstudiante, programaAcademico, semestre, promedio)
                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            
            case '4':
                print("\n--- Registrar Docente ---")
                try:
                     # capturamos los datos del usuario docente
                    nombre = input("Ingrese nombre del docente: ")
                    identificacion = input("Ingrese identificacion del docente: ")
                    correo = input("Ingresa correo electronico: ")
                    numeroEmpleado = input("Ingrese numero de empleado: ")
                    facultad = input("Ingrese facultad: ")
                    tipoContrato = input("Ingrese tipo de contratacion: ")
                    horaSemanales = input("Ingrese numero de horas semanales: ")
                    
                    # # utilizamos el controlador para agregar un nuevo docente
                    user_controller.agregar_docente(nombre, identificacion, correo, numeroEmpleado, facultad, tipoContrato, horaSemanales)
                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            
            case '5':
                print("\n--- Registrar Personal Administrativo ---")
                try:
                     # capturamos los datos del usuario administrativo
                    nombre = input("Ingrese nombre del administrativo: ")
                    identificacion = input("Ingrese identificacion del administrativo: ")
                    correo = input("Ingresa correo electronico: ")
                    numeroEmpleado = input("Ingrese numero de empleado: ")
                    dependencia = input("Ingrese dependencia: ")
                    cargo = input("Ingrese cargo: ")
                    jornada = input("Ingrese jornada: ")
                    
                    # utilizamos el controlador para agregar un nuevo administrativo
                    user_controller.agregar_administrativo(nombre, identificacion, correo, numeroEmpleado, dependencia, cargo, jornada)
                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
                    
            case '6':
                print("\n--- Registrar Grupo Academico ---")
                codigoGrupo = input("Ingrese el codigo del grupo academico: ")

                asignaturasDisponibles = asignatura_controller.get_asignaturas()
                docenteDisponibles = [p for p in user_controller.get_personas() if type(p).__name__ == 'docente']
                horariosDisponibles = horario_controller.get_horarios()

                if not asignaturasDisponibles:
                    print("No hay asignaturas registradas, debes crear una primero")
                elif not docenteDisponibles:
                    print("No hay docentes registrados, debes crear uno primero")
                elif not horariosDisponibles:
                    print("No hay horarios registrados, debes crear uno primero")
                else:
                    print("\n--- Asignaturas Disponibles ---")
                    for i, asig in enumerate(asignaturasDisponibles):
                        print(f"[{i}] Código: {asig.get_codigoAsignatura()} | Nombre: {asig.get_nombre()}")

                    print("\n--- Docentes Disponibles ---")
                    for i, docen in enumerate(docenteDisponibles):
                        print(f"[{i}] N. empleado: {docen.getNumeroDeEmpleado()} | Nombre: {docen.get_nombre()}")

                    print("\n--- Horarios Disponibles ---")
                    for i, h in enumerate(horariosDisponibles):
                        print(f"[{i}] ", end="")
                        h.mostrar_informacion()

                    asignaturaSeleccionada = None
                    try:
                        indiceAsignatura = int(input("\nSeleccione el número de la asignatura: "))
                        asignaturaSeleccionada = asignaturasDisponibles[indiceAsignatura]
                    except (ValueError, IndexError):
                        print("[Error] Selección de asignatura inválida.")

                    docenteSeleccionado = None
                    try:
                        indiceDocente = int(input("Seleccione el número del docente: "))
                        docenteSeleccionado = docenteDisponibles[indiceDocente]
                    except (ValueError, IndexError):
                        print("[Error] Selección de docente inválida.")

                    horarioSeleccionado = None
                    try:
                        indiceHorario = int(input("Seleccione el número del horario: "))
                        horarioSeleccionado = horariosDisponibles[indiceHorario]
                    except (ValueError, IndexError):
                        print("[Error] Selección de horario inválida.")

                    try:
                        capacidadGrupos = int(input("Ingresa la capacidad del grupo: "))
                    except ValueError:
                        capacidadGrupos = 0
                        print("[Error] Capacidad inválida.")

                    if asignaturaSeleccionada and docenteSeleccionado and horarioSeleccionado and capacidadGrupos > 0:
                        try:
                            grupo_academico_controller.agregar_grupo_academico(codigoGrupo, asignaturaSeleccionada, docenteSeleccionado, capacidadGrupos, horarioSeleccionado)
                            print("Grupo académico creado exitosamente con sus objetos vinculados")
                        except Exception as e:
                            print(f"[Error al crear el grupo]: {e}")
                    else:
                        print("[Error]: No se pudo crear el grupo porque alguno de los elementos seleccionados no existe o es inválido")
                    
            case '7':
                # capturamos los datos del horario
                print("\n--- Registrar Horario ---")
                try:
                
                    codigoHorario = input("Ingresa el codigo del horario: ")
                    diaHorario = input("Ingresa el día del horario: ")
                    horaIncioHorario = input("Ingresa la hora de inicio (00:00): ")
                    horaFinalHorario = input("Ingresa la hora de finalización (00:00): ")
                    salonHorario = input("Ingresa la hora de finalización: ")
                
                    # utilizamos el controlador para agregar un nuevo horario
                    horario_controller.agregar_horario(codigoHorario, diaHorario, horaIncioHorario, horaFinalHorario, salonHorario)
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            
            case '8':
                print("\n--- Matricular Estudiante ---")
                estudiantesDisponibles = [p for p in user_controller.get_personas() if type(p).__name__ == 'estudiante']

                if not estudiantesDisponibles:
                    print("No hay estudiantes registrados, debes crear uno primero")
                else:
                    print("\n--- Estudiantes Disponibles ---")
                    for i, est in enumerate(estudiantesDisponibles):
                        print(f"[{i}] Código: {est.getCodigoEstudiante()} | Nombre: {est.get_nombre()}")

                    gruposDisponibles = grupo_academico_controller.get_grupos_academicos()

                    if not gruposDisponibles:
                        print("No hay grupos académicos registrados, debes crear uno primero")
                    else:
                        print("\n--- Grupos Disponibles ---")
                        for i, grupo in enumerate(gruposDisponibles):
                            print(f"[{i}] Código: {grupo.get_codigoGrupo()} | Asignatura: {grupo.get_asignatura()} | Capacidad: {grupo.get_capacidad()}")

                        try:
                            indiceEstudiante = int(input("\nSeleccione el número del estudiante a matricular: "))
                            estudianteSeleccionado = estudiantesDisponibles[indiceEstudiante]
                        except (ValueError, IndexError):
                            estudianteSeleccionado = None
                            print("[Error] Selección de estudiante inválida.")

                        if estudianteSeleccionado is not None:
                            try:
                                indiceGrupo = int(input("Seleccione el número del grupo: "))
                                grupoSeleccionado = gruposDisponibles[indiceGrupo]
                            except (ValueError, IndexError):
                                grupoSeleccionado = None
                                print("[Error] Selección de grupo inválida.")

                            if grupoSeleccionado is not None:
                                try:
                                    grupo_academico_controller.agregar_estudiante(grupoSeleccionado.get_codigoGrupo(), estudianteSeleccionado)
                                except (EstudianteYaMatriculadoExcepcion, CapacidadMaximaExcedidaExcepcion) as e:
                                    print(f"[Error] {e}")

            case '9':
                print("\n--- Retirar Estudiante ---")
                gruposDisponibles = grupo_academico_controller.get_grupos_academicos()

                if not gruposDisponibles:
                    print("No hay grupos académicos registrados, debes crear uno primero")
                else:
                    print("\n--- Grupos Disponibles ---")
                    for i, grupo in enumerate(gruposDisponibles):
                        print(f"[{i}] Código: {grupo.get_codigoGrupo()} | Asignatura: {grupo.get_asignatura()} | Capacidad: {grupo.get_capacidad()}")

                    try:
                        indiceGrupo = int(input("\nSeleccione el número del grupo: "))
                        grupoSeleccionado = gruposDisponibles[indiceGrupo]
                    except (ValueError, IndexError):
                        grupoSeleccionado = None
                        print("[Error] Selección de grupo inválida.")

                    if grupoSeleccionado is not None:
                        estudiantesMatriculados = grupoSeleccionado.get_estudiantes_matriculados()

                        if not estudiantesMatriculados:
                            print(f"El grupo {grupoSeleccionado.get_codigoGrupo()} no tiene estudiantes matriculados.")
                        else:
                            print("\n--- Estudiantes Matriculados ---")
                            for i, est in enumerate(estudiantesMatriculados):
                                print(f"[{i}] Código: {est.getCodigoEstudiante()} | Nombre: {est.get_nombre()}")

                            try:
                                indiceEstudiante = int(input("\nSeleccione el número del estudiante a retirar: "))
                                estudianteSeleccionado = estudiantesMatriculados[indiceEstudiante]
                            except (ValueError, IndexError):
                                estudianteSeleccionado = None
                                print("[Error] Selección de estudiante inválida.")

                            if estudianteSeleccionado is not None:
                                grupo_academico_controller.retirar_estudiante(grupoSeleccionado.get_codigoGrupo(), estudianteSeleccionado.getCodigoEstudiante())
                    
            case '10':
                print("\n--- Listado de programas ---")
                mostrar_programas(programa_controller)
            
            case '11':
                print("\n--- Listado de asignaturas ---")
                mostrar_asignaturas(asignatura_controller)
                
            case '12':
                print("\n--- Listado de grupos academicos ---")
                mostrar_grupos(grupo_academico_controller)
                
            case '13':
                print("\n--- Listado de horarios ---")
                mostrar_horarios(horario_controller)
                
            case '14':
                print("\n--- Listar Estudiantes Matriculados ---")
                mostrar_estudiantes_matriculados(grupo_academico_controller)
            
            case '15':
                # mostraremos todos los usuario registrados sin importar el tipo
                print("=====================================================")
                print("   REPORTE DE USUARIOS REGISTRADOS (POLIMORFISMO)  ")
                print("=====================================================")
                mostrar_usuarios(user_controller)
                
            case '16':
                print("\n--- Buscar asignaturas ---")
                name_asignatura = input("Ingrese el nombre de la asignatura a buscar: ")
                asignaturas = asignatura_controller.buscar_asignatura_por_nombre(name_asignatura)
                if asignaturas:
                    print(f"Se encontraron {len(asignaturas)} asignatura(s) con el nombre '{name_asignatura}':")
                    for asignatura in asignaturas:
                        asignatura.mostrar_informacion()
                        print("-"*100)
                else:
                    print(f"No se encontraron asignaturas con el nombre '{name_asignatura}'.") 
                
            case '17':
                print("\n--- Buscar programas ---")
                name_programa = input("Ingrese el nombre del programa a buscar: ")
                programas = programa_controller.buscar_programa_por_nombre(name_programa)
                if programas:
                    print(f"Se encontraron {len(programas)} programa(s) con el nombre '{name_programa}':")
                    for programa in programas:
                        programa.mostrar_informacion()
                        print("-"*100)
                else:
                    print(f"No se encontraron programas con el nombre '{name_programa}'.")
            
            case '0':
                print("Salir del sistema")
                break
                
            case _:
                print("Opcion invalida, seleccione un numero del 1 al 9")
        input("\nPresione una tecla para continuar...")

if __name__ == "__main__":
    main()