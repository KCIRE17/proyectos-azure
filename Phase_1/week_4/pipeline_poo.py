import os
import csv

class PipelineLimpieza:
    # El método __init__ define las características (atributos) de nuestro pipeline
    def __init__(self, nombre_archivo):
        self.directorio = os.path.dirname(os.path.abspath(__file__))
        self.ruta_origen = os.path.join(self.directorio, nombre_archivo)
        self.ruta_destino = os.path.join(self.directorio, "datos_transformados.csv")
        self.datos = []

    # Método para EXTRAER la data
    def extraer(self):
        print(f"--- [ETAPA 1] Extrayendo datos desde: {self.ruta_origen} ---")
        try:
            with open(self.ruta_origen, "r", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                self.datos = list(lector)
            print(f"Extracción exitosa. Filas encontradas: {len(self.datos)}")
        except FileNotFoundError:
            print("Error: El archivo de origen no existe.")

    # Método para TRANSFORMAR la data (convertir texto a mayúsculas)
    def transformar(self):
        print("--- [ETAPA 2] Transformando datos (Limpieza de texto) ---")
        if not self.datos:
            print("No hay datos para transformar.")
            return
        
        # Pasamos a mayúsculas cada elemento de cada fila usando List Comprehension
        self.datos_limpios = [[columna.strip().upper() for columna in fila] for fila in self.datos]
        print("Transformación completada con éxito.")

    # Método para CARGAR la data en el destino
    def cargar(self):
        print(f"--- [ETAPA 3] Cargando datos limpios en: {self.ruta_destino} ---")
        if not hasattr(self, 'datos_limpios'):
            print("Error: Primero debes ejecutar la etapa de transformación.")
            return
            
        with open(self.ruta_destino, "w", newline="", encoding="utf-8") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerows(self.datos_limpios)
        print("¡Pipeline ejecutado e hito completado!")

# ==========================================
# USANDO NUESTRA CLASE (INSTANCIACIÓN)
# ==========================================
# Creamos el objeto 'mi_proceso' usando el plano de la Clase
mi_proceso = PipelineLimpieza("../week_3/datos_crudos.txt")

# Ejecutamos los métodos en orden (ETL)
mi_proceso.extraer()
mi_proceso.transformar()
mi_proceso.cargar()