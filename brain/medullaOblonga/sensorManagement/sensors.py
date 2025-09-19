import random

class _BaseSensor:
    name = "base"
    def __init__(self):
        self.arduino = None  # In virtual mode, no Arduino
    def connect_to_arduino(self):
        # If hardware is needed in the future, return serial object here
        return None
    def capture(self):
        return {}

class AuditorySensor(_BaseSensor):
    name = "auditory"
    def __init__(self):
        print("Trying to connect the Auditory Sensor...")
        super().__init__()
    def capture(self):
        # 0–1023 sound level
        return {"audio_level": random.randint(0, 1023)}

class VisionSensor(_BaseSensor):
    name = "vision"
    def __init__(self):
        print("Trying to connect the Vision Sensor...")
        super().__init__()
    def capture(self):
        # Only mock status
        return {"vision_status": "no_camera_virtual"}

class ProximitySensor(_BaseSensor):
    name = "proximity"
    def __init__(self):
        print("Trying to connect the Proximity Sensor...")
        super().__init__()
    def capture(self):
        # 3–120 cm
        return {"distance_cm": random.randint(3, 120)}

class TemperatureSensor(_BaseSensor):
    name = "temperature"
    def __init__(self):
        print("Trying to connect the Temperature Sensor...")
        super().__init__()
    def capture(self):
        # 18.0–34.0 °C
        return {"temp_c": round(random.uniform(18.0, 34.0), 1)}

class MovementMotor:
    def __init__(self):
        print("Trying to connect the Movement Motor...")
        self.arduino = None  # In virtual, no HW
    def move(self, direction: str):
        print(f"Moving the motor in direction: {direction}")
