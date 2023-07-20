# N: len(matrix)
# TC: O(N^2)
# SC: O(N^2)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix = [[0 for _ in range(n)] for _ in range(n)]

        r = 0
        for j in range(n - 1, - 1, - 1):
            row = matrix[r]
            idx = 0
            for i in range(n):
                new_matrix[i][j] = row[idx]
                idx += 1
            r += 1

        # print("matrix = ", matrix)
        # print("new_matrix = ", new_matrix)

        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]

        # print("matrix = ", matrix)


# ref = leetcode sample code
# N: len(matrix)
# TC: O(N^2)
# SC: O(1)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        up, bottom = 0, n - 1
        while up < bottom:
            matrix[up], matrix[bottom] = matrix[bottom], matrix[up]
            up += 1
            bottom -= 1

        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
