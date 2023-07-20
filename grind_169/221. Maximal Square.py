# M: len(matrix)
# N: len(matrix[0])
# TC: O(MN)
# SC: O(MN)


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        max_side_leng = 0
        for i in range(m):
            for j in range(n):
                max_side_leng = max(max_side_leng, dp[i][j])

        return max_side_leng * max_side_leng
