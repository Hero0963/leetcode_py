import collections


class TimeMap:
    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)
        self.max_t = collections.defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)
        self.max_t[key] = max(self.max_t[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        if timestamp >= self.max_t[key]:
            return self.values[key][-1]

        i = bisect.bisect_right(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ""

# ref = https://leetcode.com/problems/time-based-key-value-store/solutions/247130/python-concise-6-liner/
# ref = https://www.twblogs.net/a/5c4d8f63bd9eee6e7d822c35


# note:
# bisect.bisect == bisect.bisect_right True
# bisect.bisect is bisect.bisect_right False
# requirement: timestamp_prev <= timestamp, so bisect_right


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
