# M: len(heights)
# N: len(heights[0])
# TC: O(MN)
# SC: O(MN)


import collections


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        pac_set = set()
        atl_set = set()

        def helper(x, y, pre_h, ss):
            if self.visited[x][y]:
                return

            cur_h = heights[x][y]
            if cur_h < pre_h:
                return

            self.visited[x][y] = True
            ss.add((x, y))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in directions:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < m and 0 <= new_y < n:
                    helper(new_x, new_y, cur_h, ss)

        # pac_flow
        for i in range(m):
            helper(i, 0, -1, pac_set)

        for j in range(n):
            helper(0, j, -1, pac_set)

        self.visited = [[False for _ in range(n)] for _ in range(m)]
        # atl_flow
        for i in range(m):
            helper(i, n - 1, -1, atl_set)

        for j in range(n):
            helper(m - 1, j, -1, atl_set)

        # print("pac_set = ", pac_set)
        # print("atl_set = ", atl_set)

        ans = [[x, y] for (x, y) in pac_set & atl_set]
        return ans
