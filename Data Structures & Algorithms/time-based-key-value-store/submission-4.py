from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key key with the value value at the given time timestamp
        """
        self.map[key].append([value, timestamp])
        # print(f"[set] {self.map}")

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value such that set was called previously, with timestamp_prev <= timestamp
        """
        value = ""
        
        # If there are no values, it returns "".
        if key not in self.map:
            return value

        values = self.map[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(f"mid = {mid}")
            timestamp_prev = values[mid][1]
            # print(f"[get] timestamp_prev <= timestamp: {timestamp_prev} <= {timestamp}?")
            # If there are multiple such values, it returns the 
            # value associated with the largest timestamp_prev
            if timestamp_prev <= timestamp:
                value = values[mid][0]
                l = mid + 1
                # print("  yes")
            else:
                r = mid - 1
                # print("  no")
        return value
        # pass
        
# Time O()
# Space O()