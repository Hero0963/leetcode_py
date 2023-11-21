class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans = 0
        m, n = len(grid), len(grid[0])
        direction_vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x: int, y: int) -> None:
            if grid[x][y] != "1":
                return

            grid[x][y] = "0"
            for dx, dy in direction_vectors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.ans += 1
                    dfs(i, j)

        return self.ans

# M: len(grid)
# N: len(grid[0])
# TC: O(M * N)
# SC: O(M * N)
