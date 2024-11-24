# bulbo_raquideo.py

from gestiondesensores import SensorAuditivo, SensorVision, SensorProximidad, SensorTemperatura
from procesamiento import ProcesadorSensorial
from control import ControladorMotor
from memoria import GestorMemoria
import serial

def iniciando_tarjeta_madre():
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
    if not sensor_auditivo.arduino.is_open:
        print("Advertencia: Sensor auditivo no conectado. Se omitirá la captura de datos auditivos.")

    sensor_vision = SensorVision()
    if not sensor_vision.arduino.is_open:
        print("Advertencia: Sensor de visión no conectado. Se omitirá la captura de datos visuales.")

    sensor_proximidad = SensorProximidad()
    if not sensor_proximidad.arduino:
        print("Advertencia: Sensor de proximidad no conectado. Se omitirá la captura de datos de proximidad.")

    sensor_temperatura = SensorTemperatura()
    if not sensor_temperatura.arduino:
        print("Advertencia: Sensor de temperatura no conectado. Se omitirá la captura de datos de temperatura.")

    procesador = ProcesadorSensorial()
    controlador = ControladorMotor()
    gestor_memoria = GestorMemoria()

    # Lógica de operación
    if sensor_auditivo.arduino.is_open:
        procesador.iniciar_captura()  # Iniciar captura si el sensor auditivo está conectado
    if sensor_vision.arduino.is_open:
        procesador.iniciar_captura()  # Iniciar captura si el sensor de visión está conectado
    if sensor_proximidad.arduino:
        procesador.iniciar_captura()  # Iniciar captura si el sensor de proximidad está conectado
    if sensor_temperatura.arduino:
        procesador.iniciar_captura()  # Iniciar captura si el sensor de temperatura está conectado

    datos = procesador.procesar_datos_sensoriales()
    gestor_memoria.almacenar_datos_sensoriales(datos)

    decision = "mover a la derecha"  # Ejemplo de decisión
    controlador.ejecutar_accion(decision)

    if (sensor_auditivo.arduino.is_open or 
        sensor_vision.arduino.is_open or 
        sensor_proximidad.arduino or 
        sensor_temperatura.arduino):
        procesador.detener_captura()  # Detener la captura si al menos un sensor está conectado

    print("Cerebro Positronico detenido.")

if __name__ == "__main__":
    main()