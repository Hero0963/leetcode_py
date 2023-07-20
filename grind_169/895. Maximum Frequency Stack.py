import collections


# needless to update self.freq[freq -1]

class FreqStack:

    def __init__(self):
        self.record = collections.defaultdict(int)
        self.freq = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.record[val] += 1
        freq = self.record[val]
        if freq > self.max_freq:
            self.max_freq = freq

        self.freq[freq].append(val)

    def pop(self) -> int:
        res = self.freq[self.max_freq].pop()
        self.record[res] -= 1

        if not self.freq[self.max_freq]:
            self.max_freq -= 1

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


import collections


# ref = https://fuxuemingzhu.cn/leetcode/895.html#%E9%A2%98%E7%9B%AE%E6%8F%8F%E8%BF%B0

class FreqStack:

    def __init__(self):
        self.m = collections.defaultdict(int)
        self.q = []
        self.index = 0

    def push(self, x: int) -> None:
        self.m[x] += 1
        heapq.heappush(self.q, (-self.m[x], -self.index, x))
        self.index += 1

    def pop(self) -> int:
        val = heapq.heappop(self.q)[2]
        self.m[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
