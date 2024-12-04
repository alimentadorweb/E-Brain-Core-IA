# bulbo_raquideo.py
from .gestionDeSensores import SensorAuditivo, SensorVision, SensorProximidad, SensorTemperatura
from .procesamiento import ProcesadorSensorial
from .control import ControladorMotor
from .memoria import GestorMemoria
import serial  # type: ignore
import time

class BulboRaquideo:
    def __init__(self):
        # Initialization code here
        pass

def iniciando_tarjeta_madre():
    try:
        arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        print("Conexión con Arduino establecida")
        return arduino
    except serial.SerialException:
        print("Error al conectar con Arduino")
        return None

def comprobar_sensores(sensor_auditivo, sensor_vision, sensor_proximidad, sensor_temperatura):
    sensores = {
        "Sensor Auditivo": sensor_auditivo.arduino,
        "Sensor de Visión": sensor_vision.arduino,
        "Sensor de Proximidad": sensor_proximidad.arduino,
        "Sensor de Temperatura": sensor_temperatura.arduino
    }

    print("Comprobando sensores...")
    for nombre, estado in sensores.items():
        print(f"Comprobando {nombre}...")
        time.sleep(1)  # Simula el tiempo de comprobación
        
        if estado is not None:
            # Solo accede a is_open si estado no es None
            estado_str = "OK" if estado.is_open else "FALLIDO"
        else:
            estado_str = "DESCONECTADO"
        
        print(f"{nombre}: {estado_str}")
        time.sleep(0.5)  # Pausa entre comprobaciones

    print("Comprobación de sensores finalizada.\n")

def main():
    print("Iniciando el Cerebro Positronico...")

    # Inicializar componentes
    sensor_auditivo = SensorAuditivo()
    sensor_vision = SensorVision()
    sensor_proximidad = SensorProximidad()
    sensor_temperatura = SensorTemperatura()

    # Comprobar sensores
    comprobar_sensores(sensor_auditivo, sensor_vision, sensor_proximidad, sensor_temperatura)

    # Lógica de operación
    procesador = ProcesadorSensorial()
    controlador = ControladorMotor()
    gestor_memoria = GestorMemoria()

    if sensor_auditivo.arduino is not None and sensor_auditivo.arduino.is_open:
        procesador.iniciar_captura()  # Iniciar captura si el sensor auditivo está conectado
    if sensor_vision.arduino is not None and sensor_vision.arduino.is_open:
        procesador.iniciar_captura()  # Iniciar captura si el sensor de visión está conectado
    if sensor_proximidad.arduino is not None:
        procesador.iniciar_captura()  # Iniciar captura si el sensor de proximidad está conectado
    if sensor_temperatura.arduino is not None:
        procesador.iniciar_captura()  # Iniciar captura si el sensor de temperatura está conectado

    datos = procesador.procesar_datos_sensoriales()
    gestor_memoria.almacenar_datos_sensoriales(datos)

    decision = "mover a la derecha"  # Ejemplo de decisión
    controlador.ejecutar_accion(decision)

    if (sensor_auditivo.arduino is not None and sensor_auditivo.arduino.is_open or 
        sensor_vision.arduino is not None and sensor_vision.arduino.is_open or 
        sensor_proximidad.arduino is not None or 
        sensor_temperatura.arduino is not None):
        procesador.detener_captura()  # Detener la captura si al menos un sensor está conectado

    print("Cerebro Positronico detenido.")

if __name__ == "__main__":
    main()