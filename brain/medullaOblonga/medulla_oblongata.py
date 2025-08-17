# medullaOblongata/medulla_oblongata.py

from .sensorManagement import AuditorySensor, VisionSensor, ProximitySensor, TemperatureSensor
from .processing import SensoryProcessor
from .control import MotorController
from .memory import MemoryManager
import serial  # type: ignore
import time

class MedullaOblongata:
    def __init__(self):
        # Initialization code here
        pass

def initialize_motherboard():
    try:
        arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        print("Connection with Arduino established")
        return arduino
    except serial.SerialException:
        print("Error connecting to Arduino")
        return None

def check_sensors(auditory_sensor, vision_sensor, proximity_sensor, temperature_sensor):
    sensors = {
        "Auditory Sensor": auditory_sensor.arduino,
        "Vision Sensor": vision_sensor.arduino,
        "Proximity Sensor": proximity_sensor.arduino,
        "Temperature Sensor": temperature_sensor.arduino
    }

    print("Checking sensors...")
    for name, state in sensors.items():
        print(f"Checking {name}...")
        time.sleep(1)  # Simulate checking time
        
        if state is not None:
            # Only access is_open if state is not None
            state_str = "OK" if state.is_open else "FAILED"
        else:
            state_str = "DISCONNECTED"
        
        print(f"{name}: {state_str}")
        time.sleep(0.5)  # Pause between checks

    print("Sensor check completed.\n")

def main():
    print("Starting the Positronic Brain...")

    # Initialize components
    auditory_sensor = AuditorySensor()
    vision_sensor = VisionSensor()
    proximity_sensor = ProximitySensor()
    temperature_sensor = TemperatureSensor()

    # Check sensors
    check_sensors(auditory_sensor, vision_sensor, proximity_sensor, temperature_sensor)

    # Operation logic
    processor = SensoryProcessor()
    controller = MotorController()
    memory_manager = MemoryManager()

    if auditory_sensor.arduino is not None and auditory_sensor.arduino.is_open:
        processor.start_capture()  # Start capture if auditory sensor is connected
    if vision_sensor.arduino is not None and vision_sensor.arduino.is_open:
        processor.start_capture()  # Start capture if vision sensor is connected
    if proximity_sensor.arduino is not None:
        processor.start_capture()  # Start capture if proximity sensor is connected
    if temperature_sensor.arduino is not None:
        processor.start_capture()  # Start capture if temperature sensor is connected

    data = processor.process_sensory_data()
    memory_manager.store_sensory_data(data)

    decision = "move right"  # Example decision
    controller.execute_action(decision)

    if (auditory_sensor.arduino is not None and auditory_sensor.arduino.is_open or 
        vision_sensor.arduino is not None and vision_sensor.arduino.is_open or 
        proximity_sensor.arduino is not None or 
        temperature_sensor.arduino is not None):
        processor.stop_capture()  # Stop capture if at least one sensor is connected

    print("Positronic Brain stopped.")

if __name__ == "__main__":
    main()

