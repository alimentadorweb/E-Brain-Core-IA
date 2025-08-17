# control/motor_controller.py
import serial

class MotorController:
    def __init__(self):
        try:
            self.arduino = serial.Serial('COM3', 9600)  # Adjust the port according to your system
            print("Connection with Arduino established")
        except serial.SerialException as e:
            print(f"Error connecting to Arduino: {e}")
            self.arduino = None  # Set to None if connection fails

    def execute_action(self, decision):
        if self.arduino is None:
            print("Cannot execute action, Arduino is not connected.")
            return
        
        # Define logic to execute the action
        if decision == "move right":
            self.move("right")
        elif decision == "move left":
            self.move("left")
        else:
            print(f"Unknown action: {decision}")

    def move(self, direction):
        if self.arduino is not None:
            # Logic to move the motor in the specified direction
            print(f"Moving motor in direction: {direction}")
            # Example of sending a command to Arduino to move the motor
            self.arduino.write(direction.encode())
        else:
            print("Cannot move, Arduino is not connected.")
