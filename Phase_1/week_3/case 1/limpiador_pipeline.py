import csv
import os

# 1. Detectar automáticamente la carpeta donde está este script (.py)
# Esto evita que importe si estás parado en la raíz o en otra subcarpeta
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# 2. Construir las rutas absolutas uniendo la carpeta con los nombres de archivo
archivo_origen = os.path.join(directorio_actual, "datos_crudos.txt")
archivo_destino = os.path.join(directorio_actual, "datos_limpios.csv")

datos_procesados = []

print(f"Buscando archivo de origen en: {archivo_origen}")

# 3. Leer y limpiar el archivo de texto
with open(archivo_origen, "r", encoding="utf-8") as archivo:
    # Leer la primera línea (encabezados) y separarla
    encabezados = archivo.readline().strip().split(";")
    datos_procesados.append(encabezados)
    
    # Procesar el resto de filas
    for linea in archivo:
        linea = linea.strip() # Quita saltos de línea y espacios
        
        if not linea: 
            continue # Si la línea está vacía, se la salta
            
        # Separar por punto y coma y limpiar espacios de cada columna
        columnas = [col.strip() for col in linea.split(";")]
        datos_procesados.append(columnas)

# 4. Guardar los datos en un archivo CSV estándar
with open(archivo_destino, "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows(datos_procesados)

print(f"¡Pipeline ejecutado con éxito!")
print(f"Archivo guardado en: {archivo_destino}")