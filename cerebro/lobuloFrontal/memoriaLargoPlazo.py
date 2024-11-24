# lobuloFrontal/memoriaLargoPlazo.py

import os
import csv

class MemoriaLargoPlazo:
    def __init__(self, carpeta_contenedor='contenedor'):
        self.carpeta_contenedor = carpeta_contenedor
        self.datos_neuronas = {}

        # Asegúrate de que la carpeta contenedor exista
        if not os.path.exists(self.carpeta_contenedor):
            os.makedirs(self.carpeta_contenedor)

    def almacenar_datos_neurona(self, nombre_neurona, datos):
        # Almacena datos en un archivo CSV correspondiente a la neurona
        if nombre_neurona not in self.datos_neuronas:
            self.datos_neuronas[nombre_neurona] = []

        self.datos_neuronas[nombre_neurona].append(datos)

        # Guardar en el archivo CSV
        archivo_csv = os.path.join(self.carpeta_contenedor, f'{nombre_neurona}.csv')
        with open(archivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(datos)  # Escribir la fila de datos
            print(f"Datos almacenados en {archivo_csv}.")

    def obtener_datos_neurona(self, nombre_neurona):
        # Retorna los datos almacenados de una neurona específica
        archivo_csv = os.path.join(self.carpeta_contenedor, f'{nombre_neurona}.csv')
        if os.path.exists(archivo_csv):
            with open(archivo_csv, mode='r') as file:
                reader = csv.reader(file)
                return list(reader)  # Retorna todos los datos en forma de lista
        else:
            print(f"No hay datos almacenados para {nombre_neurona}.")
            return []

    def listar_neuronas(self):
        # Lista todos los archivos en la carpeta contenedor
        return [f for f in os.listdir(self.carpeta_contenedor) if f.endswith('.csv')]