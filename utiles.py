# aqui van a ir las funciones y la creacion de tabulate (pip install tabulate)

# funcion para leer los textos que el usuario añadirá
def leer_texto(mensaje):
    while True:
        texto = input(mensaje)
        if texto != "":
            return texto
        print("Escriba algo: ")

# leer_int para los números y las puntuaciones
def leer_int(mensaje):
    numero = int(input(mensaje))
    return numero

#generar_id para el buscar id y eliminar id 
def generar_id(lista):
    if len(lista) == 0:
        return 1
    else:
        # Último ID + 1
        return lista[-1]["id"] + 1
    
#Mostrar las tablas
def imprimir_tabla(filas, columnas):
    print(columnas) #mostrar las columnas
    for fila in filas:
        print(fila) #mostar cada dato
