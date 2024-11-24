# memoria/gestor_memoria.py

from lobuloFrontal.memoriaCortoPlazo import MemoriaCortoPlazo

class GestorMemoria:
    def __init__(self):
        self.datos_sensoriales = []
        self.decisiones = []
        self.memoria_corto_plazo = MemoriaCortoPlazo()  # Instancia de memoria a corto plazo

    def almacenar_datos_sensoriales(self, datos):
        self.datos_sensoriales.append(datos)
        self.memoria_corto_plazo.almacenar(datos)  # Almacenar en memoria a corto plazo
        print("Datos sensoriales almacenados.")

    def obtener_datos_recientes(self):
        # Retorna los últimos datos sensoriales
        return self.datos_sensoriales[-1] if self.datos_sensoriales else None

    def almacenar_decision(self, decision):
        self.decisiones.append(decision)
        print("Decisión almacenada.")

    def obtener_ultima_decision(self):
        # Retorna la última decisión tomada
        return self.decisiones[-1] if self.decisiones else None