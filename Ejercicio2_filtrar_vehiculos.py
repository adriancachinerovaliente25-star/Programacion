vehiculos = [{"vehiculo": "Moto", "revision": "pendiente"},
             {"vehiculo": "Camión", "revision": "aprobada"}
]

# Función
def revision_aprobada(v):
    return v["revision"] == "aprobada"

vehiculos_aprobados = list(filter(revision_aprobada, vehiculos))
print(vehiculos_aprobados)