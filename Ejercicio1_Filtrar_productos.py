# Lista de productos del almacén
productos = ["manzana", "arroz", "zanahoria", "fideos", "lechuga", "lentejas"]

# Función para filtrar productos perecederos
def es_perecedero(producto):
    productos_perecederos = ["manzana", "zanahoria", "lechuga"]
    return producto in productos_perecederos

productos_filtrados = list(filter(es_perecedero, productos))
print(productos_filtrados)
