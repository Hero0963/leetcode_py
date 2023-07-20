# M: len(grid)
# N: len(grid[0])
# TC: O(MN)
# SC: O(MN)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        que = collections.deque()
        fresh_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append([i, j])
                if grid[i][j] == 1:
                    fresh_cnt += 1

        minutes = 0
        direction_vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while que:
            l = len(que)
            for _ in range(l):
                x, y = que.popleft()
                for d in direction_vectors:
                    new_x, new_y = x + d[0], y + d[1]
                    if 0 <= new_x < m and 0 <= new_y < n:
                        if grid[new_x][new_y] == 1:
                            que.append([new_x, new_y])
                            grid[new_x][new_y] = 2
                            fresh_cnt -= 1

            minutes += 1

        if fresh_cnt:
            return -1

        return max(0, minutes - 1)





