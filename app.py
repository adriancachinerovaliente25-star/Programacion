from equipos import menu_equipos
from jugadores import menu_jugadores

def menu_principal():
    opcion = 0
    while opcion != 3:
        print("MENÚ PRINCIPAL")
        print("1. Gestión de equipos")
        print("2. Gestión de jugadores")
        print("3. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            menu_equipos()
        elif opcion == 2:
            menu_jugadores()
        elif opcion == 3:
            print("Adiossss...")
        else:
            print("Opción no válida")

menu_principal()
