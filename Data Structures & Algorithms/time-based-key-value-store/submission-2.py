from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.values[key]
        print('***')
        print('key', candidates, timestamp)
        if not candidates:
            return ""

        res = ""
        l, r = 0, len(candidates) - 1
        while l <= r:
            m = (l + r) // 2

            if candidates[m][0] <= timestamp:
                print('moving l to m')
                l = m + 1
                res = candidates[m][1]
            else:
                print('moving r to m')
                r = m - 1
        
        return res