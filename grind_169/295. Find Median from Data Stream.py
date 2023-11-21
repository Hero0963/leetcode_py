# ref= https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            val = -heappushpop(self.small, -num)
            heappush(self.large, val)
        else:
            val = -heappushpop(self.large, num)
            heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.sorted_list = SortedList()

    def addNum(self, num: int) -> None:
        self.sorted_list.add(num)

    def findMedian(self) -> float:
        n = len(self.sorted_list)
        if n % 2 == 0:
            mid1 = self.sorted_list[n // 2 - 1]
            mid2 = self.sorted_list[n // 2]
            return (mid1 + mid2) / 2.0
        else:
            return float(self.sorted_list[n // 2])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
