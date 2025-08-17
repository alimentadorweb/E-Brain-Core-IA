# frontalLobe/longTermMemory.py

import os
import csv

class LongTermMemory:
    def __init__(self, container_folder='container'):
        self.container_folder = container_folder
        self.neuron_data = {}

        # Ensure the container folder exists
        if not os.path.exists(self.container_folder):
            os.makedirs(self.container_folder)

    def store_neuron_data(self, neuron_name, data):
        # Store data in a CSV file corresponding to the neuron
        if neuron_name not in self.neuron_data:
            self.neuron_data[neuron_name] = []

        self.neuron_data[neuron_name].append(data)

        # Save to CSV file
        csv_file = os.path.join(self.container_folder, f'{neuron_name}.csv')
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)  # Write the data row
            print(f"Data stored in {csv_file}.")

    def get_neuron_data(self, neuron_name):
        # Return the stored data of a specific neuron
        csv_file = os.path.join(self.container_folder, f'{neuron_name}.csv')
        if os.path.exists(csv_file):
            with open(csv_file, mode='r') as file:
                reader = csv.reader(file)
                return list(reader)  # Return all data as a list
        else:
            print(f"No data stored for {neuron_name}.")
            return []

    def list_neurons(self):
        # List all CSV files in the container folder
        return [f for f in os.listdir(self.container_folder) if f.endswith('.csv')]
