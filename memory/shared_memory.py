import time

class SharedMemory:
    def __init__(self):
        self.storage = {}

    def store(self, key, value):
        timestamp = time.time()
        self.storage[key] = {
            "value": value,
            "timestamp": timestamp
        }
        print(f"[Memory] Stored key={key} at {timestamp}")

    def retrieve(self, key):
        return self.storage.get(key)
