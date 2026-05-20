import json
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_json = os.path.join(directorio_actual, "reporte_config.json")

# Leer el archivo JSON
with open(ruta_json, "r", encoding="utf-8") as archivo:
    config = json.load(archivo) # Convierte el JSON en un diccionario de Python

# Acceder a los datos como lo aprendiste en el Bloque 3
print(f"Pipeline a ejecutar: {config['pipeline_name']}")

# Modificar un dato en memoria
config['retry_attempts'] = 5

# Guardar los cambios en un nuevo archivo
ruta_salida = os.path.join(directorio_actual, "reporte_config_actualizado.json")
with open(ruta_salida, "w", encoding="utf-8") as archivo_salida:
    json.dump(config, archivo_salida, indent=4)

print("¡Archivo JSON actualizado y guardado!")