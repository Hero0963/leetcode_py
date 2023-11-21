class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = [0] * (m * n)
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        corner = [[0, n - 1], [m - 1, n - 1], [m - 1, 0], [1, 0]]
        corner_renew = [[1, -1], [-1, -1], [-1, 1], [1, 1]]
        pos = [0, 0]
        idx = 0
        total = m * n

        while idx < total:
            i, j = pos
            ans[idx] = matrix[i][j]
            idx += 1

            if pos == corner[d]:
                corner[d][0] += corner_renew[d][0]
                corner[d][1] += corner_renew[d][1]
                d = (d + 1) % 4

            pos[0] += direction[d][0]
            pos[1] += direction[d][1]

        return ans

# M, N = len(matrix), len(matrix[0])
# TC: O(MN)
# SC: O(MN), ans as return, remaining: O(1)
