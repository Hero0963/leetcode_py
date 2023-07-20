# M: len(grid)
# N: len(grid[0])
# TC: O(M * N)
# SC: O(1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            if grid[i][j] != "1":
                return

            grid[i][j] = "0"
            direction_vectors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for v in direction_vectors:
                x, y = i + v[0], j + v[1]
                if 0 <= x < m and 0 <= y < n:
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.ans += 1
                    dfs(i, j)

        return self.ans
