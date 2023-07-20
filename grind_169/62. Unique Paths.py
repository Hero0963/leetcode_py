# M: m
# N: n
# TC: O(MN)
# SC: O(MN)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


# K : min(m, n)
# TC: O(K)
# SC: O(1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = m + n - 2
        b = min(m, n) - 1
        ans = math.comb(a, b)
        return ans
