# ref = https://leetcode.cn/problems/01-matrix/solution/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-2/
# ref2 DP = https://leetcode.com/problems/01-matrix/solutions/1369741/c-java-python-bfs-dp-solutions-with-picture-clean-concise-o-1-space/
from typing import List
import collections


class Solution:
    """
    M, N = len(mat), len(mat[0])
    time complexity: O(MN)
    space complexity: O(MN)
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = collections.deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = True

        dirs = [[0, 1], [0, - 1], [1, 0], [- 1, 0]]
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if mat[x][y] == 1:
                    res[x][y] = step

                for dx, dy in dirs:
                    new_x, new_y = x + dx, y + dy
                    if (new_x < 0 or new_x >= m) or (new_y < 0 or new_y >= n) or (visited[new_x][new_y]):
                        continue

                    queue.append([new_x, new_y])
                    visited[new_x][new_y] = True

            step += 1

        return res
