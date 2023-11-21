class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(x, y, prev):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0

            cur_val = matrix[x][y]
            if cur_val <= prev:
                return 0

            if dp[x][y] != -1:
                return dp[x][y]

            left = dfs(x, y - 1, cur_val)
            right = dfs(x, y + 1, cur_val)
            top = dfs(x - 1, y, cur_val)
            bottom = dfs(x + 1, y, cur_val)

            dp[x][y] = max(left, right, top, bottom) + 1
            return dp[x][y]

        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -math.inf))

        return ans

# M: len(matrix)
# N: len(matrix[0])
# TC: O(MN)
# SC: O(MN)
