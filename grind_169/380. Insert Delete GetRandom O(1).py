class RandomizedSet:

    def __init__(self):
        self.vals = defaultdict(int)
        self.idxs = []

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False

        self.vals[val] = len(self.idxs)
        self.idxs.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False

        last_ele = self.idxs[-1]
        remove_pos = self.vals[val]

        self.vals[last_ele] = remove_pos
        self.idxs[remove_pos] = last_ele

        del self.vals[val]
        self.idxs.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.idxs)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()