# N: n
# TC: O(N)
# SC: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        pre2, pre = 1, 2
        for _ in range(3, n + 1):
            res = pre2 + pre
            pre2 = pre
            pre = res

        return res
