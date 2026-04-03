# Pattern: Binary Search on sorted timestamps — find largest timestamp <= given timestamp
# Trigger: "get value at or before timestamp" = sorted timestamps = binary search for floor value

class TimeMap:
    def __init__(self):
        self.keyStore = {}     # key: list of [value, timestamp] in ascending timestamp order

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])  # timestamps always increasing

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]     # valid candidate — try to find a later one
                l = m + 1
            else:
                r = m - 1              # timestamp too large — go left
        return res                     # best valid value found or "" if none
    