# Importamos las funciones del archivo utiles.py y del equipo.py 
from utiles import leer_int, leer_texto, generar_id
from equipos import equipos

# Lista donde se guardarán todos los jugadores
jugadores = []

# Crear jugador
def crear_jugador():
    print("Crear jugador")
    nombre = leer_texto("Nombre del jugador: ")
    edad = leer_int("Edad del jugador: ")
    equipo_id = leer_int("ID del equipo al que pertenece: ")

# Verificar si el equipo existe y está activo
    for equipo in equipos:
        if equipo["id"] == equipo_id and equipo["activo"]:
            nuevo_jugador = {
                "id": generar_id(jugadores),
                "nombre": nombre,
                "edad": edad,
                "equipo_id": equipo_id,
                "activo": True
            }
            jugadores.append(nuevo_jugador)
            print("Jugador creado:", nuevo_jugador)
            return
    print("No se pudo crear el jugador (equipo no existe o está inactivo)")

# Listar solo jugadores activos
def listar_jugadores():
    print("Lista de jugadores activos:")
    for jugador in jugadores:
        if jugador["activo"]:
            nombre_equipo = "Sin equipo"
            for equipo in equipos:
                if equipo["id"] == jugador["equipo_id"]:
                    nombre_equipo = equipo["nombre"]
            print(f"ID: {jugador['id']} - Nombre: {jugador['nombre']} - Edad: {jugador['edad']} - Equipo: {nombre_equipo}")

# Buscar jugador por ID
def buscar_jugador():
    print("Buscar jugador")
    id_buscar = leer_int("ID del jugador: ")

    for jugador in jugadores:
        if jugador["id"] == id_buscar:
            if jugador["activo"]:
                print(f"ID: {jugador['id']} - Nombre: {jugador['nombre']} - Edad: {jugador['edad']} - Equipo ID: {jugador['equipo_id']}")
            else:
                print("El jugador existe, pero está inactivo.")
            return

    print("No se encontró un jugador con ese ID.")

# Actualizar jugador
def actualizar_jugador():
    print("Actualizar jugador")
    id_editar = leer_int("ID del jugador a actualizar: ")

    for jugador in jugadores:
        if jugador["id"] == id_editar:
            if jugador["activo"]:
                nuevo_nombre = leer_texto("Nuevo nombre: ")
                nueva_edad = leer_int("Nueva edad: ")
                jugador["nombre"] = nuevo_nombre
                jugador["edad"] = nueva_edad
                print("Jugador actualizado correctamente")
            else:
                print("No se puede editar un jugador inactivo.")
            return

    print("No existe un jugador con ese ID.")

# Eliminar jugador (inactivar)
def eliminar_jugador():
    print("Eliminar jugador")
    id_eliminar = leer_int("ID del jugador: ")

    for jugador in jugadores:
        if jugador["id"] == id_eliminar:
            jugador["activo"] = False
            print("Jugador desactivado:", jugador)
            return

    print("Ese ID no existe")


#menu de los jugadores
def menu_jugadores():
    opcion = 0
    while opcion != 6:
        print("MENÚ GESTIÓN DE JUGADORES")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Buscar jugador")
        print("4. Actualizar jugador")
        print("5. Eliminar jugador")
        print("6. Volver al menú principal")

        opcion = leer_int("Seleccione una opción: ")

        if opcion == 1:
            crear_jugador()
        elif opcion == 2:
            listar_jugadores()
        elif opcion == 3:
            buscar_jugador()
        elif opcion == 4:
            actualizar_jugador()
        elif opcion == 5:
            eliminar_jugador()
        elif opcion == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, intente de nuevo")
