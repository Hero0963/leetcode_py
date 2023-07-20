import collections
import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        self._sum = sum(w)
        n = len(w)
        prefix_sum = [0] * n
        prefix_sum[0] = w[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + w[i]

        self.prefix_sum = prefix_sum

    def pickIndex(self) -> int:
        goal = random.randint(1, self._sum)
        idx = bisect.bisect_left(self.prefix_sum, goal)
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# note we can apply Alias method to improve the pickIndex search idx efficient
# https://leetcode.com/problems/random-pick-with-weight/solutions/671439/python-smart-o-1-solution-with-detailed-explanation/