# control/controlador_motor.py
import serial

class ControladorMotor:
    def __init__(self):
        self.arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Ajusta el puerto según tu sistema

    def ejecutar_accion(self, decision):
        self.arduino.write(decision.encode() + b'\n')
        print(f"Ejecutando acción: {decision}")