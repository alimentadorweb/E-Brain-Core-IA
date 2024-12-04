# procesamiento/procesador_sensorial.py

from cerebro.bulboRaquideo.gestionDeSensores.sensores import SensorAuditivo, SensorVision, SensorProximidad, SensorTemperatura

class ProcesadorSensorial:
    def __init__(self):
        self.sensor_auditivo = SensorAuditivo()
        self.sensor_vision = SensorVision()
        self.sensor_proximidad = SensorProximidad()
        self.sensor_temperatura = SensorTemperatura()

    def iniciar_captura(self):
        print("Iniciando captura de datos sensoriales...")

    def detener_captura(self):
        print("Deteniendo captura de datos sensoriales...")

    def procesar_datos_sensoriales(self):
        # Captura datos de todos los sensores
        datos_auditivos = self.sensor_auditivo.capturar() if self.sensor_auditivo.arduino and self.sensor_auditivo.arduino.is_open else "Sensor auditivo no conectado"
        datos_visuales = self.sensor_vision.capturar() if self.sensor_vision.arduino and self.sensor_vision.arduino.is_open else "Sensor de visión no conectado"
        datos_proximidad = self.sensor_proximidad.capturar() if self.sensor_proximidad.arduino else "Sensor de proximidad no conectado"
        datos_temperatura = self.sensor_temperatura.capturar() if self.sensor_temperatura.arduino else "Sensor de temperatura no conectado"

        return {
            'auditivo': datos_auditivos,
            'visual': datos_visuales,
            'proximidad': datos_proximidad,
            'temperatura': datos_temperatura
        }