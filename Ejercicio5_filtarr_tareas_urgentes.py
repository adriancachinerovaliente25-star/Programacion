# Lista de tareas
tareas = [
    {"tarea": "Enviar informe", "urgente": True}
]
# Función
def es_urgente(t):
    return t["urgente"] == True

tareas_urgentes = list(filter(es_urgente, tareas))
print(tareas_urgentes)
