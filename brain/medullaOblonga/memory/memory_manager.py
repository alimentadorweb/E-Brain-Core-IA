from ...frontalLobe.shortTermMemory import ShortTermMemory

class MemoryManager:
    def __init__(self):
        self.sensory_data = []
        self.decisions = []
        self.short_term_memory = ShortTermMemory()  # Instance of short-term memory

    def store_sensory_data(self, data):
        self.sensory_data.append(data)
        self.short_term_memory.store(data)  # Store in short-term memory
        print("Sensory data stored.")

    def get_recent_data(self):
        # Return the latest sensory data
        return self.sensory_data[-1] if self.sensory_data else None

    def store_decision(self, decision):
        self.decisions.append(decision)
        print("Decision stored.")

    def get_last_decision(self):
        # Return the last decision taken
        return self.decisions[-1] if self.decisions else None
