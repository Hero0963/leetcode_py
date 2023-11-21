from typing import List
import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = collections.deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True

        dirs = [(0, 1), (0, - 1), (1, 0), (- 1, 0)]
        distance = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if mat[x][y] == 1:
                    res[x][y] = distance

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or nx >= m) or (ny < 0 or ny >= n) or (visited[nx][ny]):
                        continue

                    queue.append([nx, ny])
                    visited[nx][ny] = True

            distance += 1

        return res

# M, N = len(mat), len(mat[0])
# TC: O(NM)
# SC: O(NM)
# note: DP solution can reduce SC to O(1)
# ref = https://leetcode.cn/problems/01-matrix/solutions/202012/01ju-zhen-by-leetcode-solution/