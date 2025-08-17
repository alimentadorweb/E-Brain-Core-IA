from neural_network import Neuron

class Neuro(Neuron):
    def __init__(self):
        super().__init__(weight=0.3)  # Different weight for n3

    def activate(self, input_data, command, human_damage):
        # Specific logic for n3
        print("Activating neuron n3")
        
        # Call the activation method from the base class
        activation = super().activate(input_data, command, human_damage)

        # Store the memory of the activation
        self.store_memory(activation)
        
        return activation

    def store_memory(self, activation):
        # Logic to store the memory
        directory_path = "memories"  # Folder where memories will be saved
        file_name = f"{directory_path}/memory_n3.csv"

        # Create directory if it does not exist
        import os
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(file_name, "a") as f:
            f.write(f"{activation}\n")  # Store the activation in a file
            print(f"Memory stored in: {file_name}")
