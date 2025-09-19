# processing/sensory_processor.py

from ..sensorManagement.sensors import (
    AuditorySensor,
    VisionSensor,
    ProximitySensor,
    TemperatureSensor,
)


class SensoryProcessor:
    def __init__(self):
        print("Initializing Sensory Processor...")
        self.auditory_sensor = AuditorySensor()
        self.vision_sensor = VisionSensor()
        self.proximity_sensor = ProximitySensor()
        self.temperature_sensor = TemperatureSensor()

    def start_capture(self):
        print("Starting sensory data capture...")

    def stop_capture(self):
        print("Stopping sensory data capture...")

    def process_sensory_data(self):
        # Capture data from all sensors
        auditory_data = (
            self.auditory_sensor.capture()
            if self.auditory_sensor.arduino and self.auditory_sensor.arduino.is_open
            else "Auditory sensor not connected"
        )
        visual_data = (
            self.vision_sensor.capture()
            if self.vision_sensor.arduino and self.vision_sensor.arduino.is_open
            else "Vision sensor not connected"
        )
        proximity_data = (
            self.proximity_sensor.capture()
            if self.proximity_sensor.arduino
            else "Proximity sensor not connected"
        )
        temperature_data = (
            self.temperature_sensor.capture()
            if self.temperature_sensor.arduino
            else "Temperature sensor not connected"
        )

        print("Sensory data captured successfully.")

        return {
            "auditory": auditory_data,
            "visual": visual_data,
            "proximity": proximity_data,
            "temperature": temperature_data,
        }
