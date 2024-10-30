# procesamiento/procesador_sensorial.py

from .gestiondesensores.sensores import SensorAuditivo, SensorVision

class ProcesadorSensorial:
    def __init__(self):
        self.sensor_auditivo = SensorAuditivo()
        self.sensor_vision = SensorVision()

    def iniciar_captura(self):
        print("Iniciando captura de datos sensoriales...")

    def detener_captura(self):
        print("Deteniendo captura de datos sensoriales...")

    def procesar_datos_sensoriales(self):
        # Captura datos de ambos sensores
        datos_auditivos = self.sensor_auditivo.capturar()
        datos_visuales = self.sensor_vision.capturar()
        return {
            'auditivo': datos_auditivos,
            'visual': datos_visuales
        }