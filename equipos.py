#  Usamos el imspor para poder usar las funciones del utiles.py
from utiles import leer_int, leer_texto, generar_id

#Una lista para guardar todos los datos de los equipos
equipos = []

#creamos una lista pea listar los equipos que no puedo sino
activos = []
#funciones 

# el menu de los equipos
def menu_equipos():
    opcion = 0
    while opcion != 6:
        print("MENÚ GESTIÓN DE EQUIPOS")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo")
        print("4. Actualizar equipo")
        print("5. Eliminar equipo")
        print("6. Volver al menú principal")

        opcion = leer_int("Seleccione una opción: ")

        if opcion == 1:
            crear_equipos()
        elif opcion == 2:
            listar_equipos()
        elif opcion == 3:
            buscar_equipo()
        elif opcion == 4:
            actualizar_equipo()
        elif opcion == 5:
            eliminar_equipo()
        elif opcion == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida, intente de nuevo")
#funcion para crear los equipos
def crear_equipos():
    print("Crear equipo")
    nombre = leer_texto("nombre del equipo: ")
    ciudad = leer_texto("Nombre de la ciudad: ")
    nuevo_equipo = {
        "id": generar_id(equipos),
        "nombre": nombre,
        "ciudad": ciudad,
        "activo": True
    }
    equipos.append(nuevo_equipo)
    print("Equipo creado")

# Listar equipos (solo los activos)
def listar_equipos():
    print("Lista de equipos")
    encontrados = 0
    for equipo in equipos:
        if equipo["activo"]:
            print(f"ID: {equipo['id']} - Nombre: {equipo['nombre']} - Ciudad: {equipo['ciudad']}")
            encontrados += 1
    if encontrados == 0:
        print("No hay equipos activos.")


# funcion para buscar los equipos
def buscar_equipo():
    print("Buscar equipo")
    id_buscar = leer_int("ID del equipo: ")

    for equipo in equipos:
        if equipo["id"] == id_buscar:        # Primero reviso si el ID coincide
            if equipo["activo"]:            # Luego reviso si está activo
                print("ID:", equipo["id"], "Nombre:", equipo["nombre"], "Ciudad:", equipo["ciudad"])
                return
            else:
                print("El equipo existe, pero está inactivo.")
                return

    print("No se encontró un equipo con ese ID.")

# funcion para actualizar el equipo
def actualizar_equipo():
    print("Actualizar equipo")
    id_editar = leer_int("ID del equipo que desea actualizar: ")

    for equipo in equipos:
        if equipo["id"] == id_editar:        # Primero reviso si el ID coincide
            if equipo["activo"]:            # Luego reviso si está activo
                nuevo_nombre = leer_texto("Nuevo nombre:")
                nueva_ciudad = leer_texto("Nueva ciudad:")
                equipo["nombre"] = nuevo_nombre
                equipo["ciudad"] = nueva_ciudad
                print("El equipo ha sido actulizado correctamente")
                return
            else:
                print("No se ha podido editar (Inactivo)")
                return

    print("No se encontró un equipo con ese ID.")

# eliminar un equipo o ponerlo inactivo
def eliminar_equipo():
    print("Eliminar equipo")
    id_eliminar = leer_int("Ingrese el ID que busca: ")
    for equipo in equipos:
        if equipo["id"] == id_eliminar:
            equipo["activo"] = False
            print("Equipo desactivado:", equipo)
            return
    print("Ese ID no existe")


