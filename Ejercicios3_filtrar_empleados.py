# Lista de empleado
empleados = [
    {"nombre": "Ana", "estado": "activo"}
]
# Función
def empleado_activo(e):
    return e["estado"] == "activo"

empleados_activos = list(filter(empleado_activo, empleados))
print(empleados_activos)
