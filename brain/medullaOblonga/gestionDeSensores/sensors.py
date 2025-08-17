# sensores.py
import random

class _BaseSensor:
    name = "base"
    def __init__(self):
        self.arduino = None  # En virtual no hay Arduino
    def conectar_a_arduino(self):
        # Si en el futuro necesitas HW, retorna objeto serial aquí
        return None
    def capturar(self):
        return {}

class SensorAuditivo(_BaseSensor):
    name = "auditivo"
    def __init__(self):
        print("Intentando conectar el sensor auditivo...")
        super().__init__()
    def capturar(self):
        # 0–1023 nivel de sonido
        return {"audio_level": random.randint(0, 1023)}

class SensorVision(_BaseSensor):
    name = "vision"
    def __init__(self):
        print("Intentando conectar el sensor de Visión...")
        super().__init__()
    def capturar(self):
        # Solo mock de estado
        return {"vision_status": "no_camera_virtual"}

class SensorProximidad(_BaseSensor):
    name = "proximidad"
    def __init__(self):
        print("Intentando conectar el sensor Proximidad...")
        super().__init__()
    def capturar(self):
        # 3–120 cm
        return {"distance_cm": random.randint(3, 120)}

class SensorTemperatura(_BaseSensor):
    name = "temperatura"
    def __init__(self):
        print("Intentando conectar el sensor Temperatura...")
        super().__init__()
    def capturar(self):
        # 18.0–34.0 °C
        return {"temp_c": round(random.uniform(18.0, 34.0), 1)}

class MotorMovimiento:
    def __init__(self):
        print("Intentando conectar el sensor Movimiento...")
        self.arduino = None  # En virtual, sin HW
    def mover(self, direccion: str):
        print(f"Moviendo el motor en la dirección: {direccion}")
