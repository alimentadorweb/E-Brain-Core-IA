# control/controlador_motor.py
import serial

class ControladorMotor:
    def __init__(self):
        try:
            self.arduino = serial.Serial('COM3', 9600)  # Ajusta el puerto según tu sistema
            print("Conexión con Arduino establecida")
        except serial.SerialException as e:
            print(f"Error al conectar con Arduino: {e}")
            self.arduino = None  # Establecer a None si no se puede conectar

    def ejecutar_accion(self, decision):
        if self.arduino is None:
            print("No se puede ejecutar la acción, Arduino no está conectado.")
            return
        
        # Aquí puedes definir la lógica para ejecutar la acción
        if decision == "mover a la derecha":
            self.mover("derecha")
        elif decision == "mover a la izquierda":
            self.mover("izquierda")
        else:
            print(f"Acción desconocida: {decision}")

    def mover(self, direccion):
        if self.arduino is not None:
            # Lógica para mover el motor en la dirección especificada
            print(f'Moviendo el motor en la dirección: {direccion}')
            # Aquí podrías enviar un comando al Arduino para mover el motor
            self.arduino.write(direccion.encode())  # Ejemplo de cómo enviar un comando
        else:
            print("No se puede mover, Arduino no está conectado.")