import collections


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

# needless to update self.freq[freq -1]
