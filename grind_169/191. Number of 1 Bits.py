# N: bits of n, here N < 33
# TC: O(N)
# SC: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            if n & 1:
                cnt += 1
            n = n >> 1
        return cnt


# N: bits of n, here N < 33
# TC: O(N)
# SC: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            n, r = divmod(n, 2)
            if r == 1:
                cnt += 1

        return cnt
