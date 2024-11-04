# bulbo_raquideo.py

from gestiondesensores import SensorAuditivo, SensorVision
from procesamiento import ProcesadorSensorial
from control import ControladorMotor
from memoria import GestorMemoria
import serial

def inicializar_arduino():
    try:
        arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        print("Conexión con Arduino establecida")
        return arduino
    except serial.SerialException:
        print("Error al conectar con Arduino")
        return None
    
def main():
    print("Iniciando el Cerebro Positronico...")
    
    # Inicializar componentes
    sensor_auditivo = SensorAuditivo()
    sensor_vision = SensorVision()
    procesador = ProcesadorSensorial()
    controlador = ControladorMotor()
    gestor_memoria = GestorMemoria()
    
    # Lógica de operación
    procesador.iniciar_captura()
    datos = procesador.procesar_datos_sensoriales()
    gestor_memoria.almacenar_datos_sensoriales(datos)
    
    decision = "mover a la derecha"  # Ejemplo de decisión
    controlador.ejecutar_accion(decision)
    
    procesador.detener_captura()
    print("Cerebro Positronico detenido.")

if __name__ == "__main__":
    main()