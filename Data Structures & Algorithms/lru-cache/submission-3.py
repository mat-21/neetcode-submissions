from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        self.usage = deque()

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        self.usage.remove(key)
        self.usage.append(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key] = value
            self.usage.remove(key)
            self.usage.append(key)
            return

        self.values[key] = value
        self.usage.append(key)

        if len(self.values) > self.capacity:
            # remove from usage and then values
            lru = self.usage.popleft()
            self.values.pop(lru)
