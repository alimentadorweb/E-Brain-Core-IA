# frontalLobe/shortTermMemory.py

class ShortTermMemory:
    def __init__(self):
        self.data = []

    def store(self, data):
        self.data.append(data)
        print("Data stored in short-term memory.")

    def get_data(self):
        return self.data
