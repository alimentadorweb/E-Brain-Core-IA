# gestiondesensores/sensores.py

import serial

class SensorAuditivo:
    def __init__(self):
        self.arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Ajusta el puerto según tu sistema
    
    def capturar(self):
        self.arduino.write(b'AUDIO\n')  # Comando para Arduino
        datos = self.arduino.readline()
        return f"Datos auditivos capturados: {datos.decode().strip()}"

class SensorVision:
    def __init__(self):
        self.arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Ajusta el puerto según tu sistema
    
    def capturar(self):
        self.arduino.write(b'VISION\n')  # Comando para Arduino
        datos = self.arduino.readline()
        return f"Datos visuales capturados: {datos.decode().strip()}"

class MotorMovimiento:
    def mover(self, accion):
        # Lógica para mover el motor según la acción
        print(f"Ejecutando acción: {accion}")