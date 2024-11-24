# lobuloFrontal/memoriaCortoPlazo.py

class MemoriaCortoPlazo:
    def __init__(self):
        self.datos = []

    def almacenar(self, datos):
        self.datos.append(datos)
        print("Datos almacenados en memoria a corto plazo.")

    def obtener_datos(self):
        return self.datos