# bulboraquideo/bulbo_raquideo.py

import threading
import time
from .gestiondesensores.sensores import SensorAuditivo, MotorMovimiento, SensorVision
from .procesamiento.procesador_sensorial import ProcesadorSensorial
from .control.controlador_motor import ControladorMotor
from .memoria.gestor_memoria import GestorMemoria

class BulboRaquideo:
    def __init__(self):
        self.procesador_sensorial = ProcesadorSensorial()
        self.controlador_motor = ControladorMotor()
        self.gestor_memoria = GestorMemoria()
        self.ejecutando = False

    def iniciar(self):
        print("Iniciando Cerebro Positrónico...")
        self.ejecutando = True
        self.procesador_sensorial.iniciar_captura()
        threading.Thread(target=self._ciclo_principal, daemon=True).start()

    def detener(self):
        print("Deteniendo Cerebro Positrónico...")
        self.ejecutando = False
        self.procesador_sensorial.detener_captura()

    def _ciclo_principal(self):
        while self.ejecutando:
            self._procesar_entradas()
            self._tomar_decisiones()
            self._ejecutar_acciones()
            time.sleep(0.01)  # Pequeña pausa para no saturar el CPU

    def _procesar_entradas(self):
        datos_sensoriales = self.procesador_sensorial.procesar_datos_sensoriales()
        self.gestor_memoria.almacenar_datos_sensoriales(datos_sensoriales)

    def _tomar_decisiones(self):
        datos_recientes = self.gestor_memoria.obtener_datos_recientes()
        # Aquí iría la lógica de toma de decisiones
        decision = self._analizar_datos(datos_recientes)
        self.gestor_memoria.almacenar_decision(decision)

    def _ejecutar_acciones(self):
        ultima_decision = self.gestor_memoria.obtener_ultima_decision()
        self.controlador_motor.ejecutar_accion(ultima_decision)

    def _analizar_datos(self, datos):
        # Implementa aquí tu lógica de análisis y toma de decisiones
        return "Decisión basada en el análisis de datos"

# Punto de entrada del programa
if __name__ == "__main__":
    cerebro = BulboRaquideo()
    try:
        cerebro.iniciar()
        # Mantén el programa en ejecución
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cerebro.detener()
        print("Cerebro Positrónico detenido.")