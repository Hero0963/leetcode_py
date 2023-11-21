import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty_cell = 0
        fresh_orange = 1
        rotten_orange = 2

        m, n = len(grid), len(grid[0])
        que = collections.deque()
        fresh_cnt = 0
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == rotten_orange:
                    que.append((i, j))
                if cell == fresh_orange:
                    fresh_cnt += 1

        if not fresh_cnt:
            return 0

        minutes = -1
        direction_vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while que:
            minutes += 1
            l = len(que)
            for _ in range(l):
                x, y = que.popleft()
                for dx, dy in direction_vectors:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        next_cell = grid[nx][ny]
                        if next_cell == fresh_orange:
                            que.append((nx, ny))
                            grid[nx][ny] = rotten_orange
                            fresh_cnt -= 1

        return minutes if not fresh_cnt else -1

# M: len(grid)
# N: len(grid[0])
# TC: O(MN)
# SC: O(MN)
