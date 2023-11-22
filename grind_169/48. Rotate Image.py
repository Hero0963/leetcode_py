class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def rotate_points_on_cur_ring(i, steps):
            for j in range(steps):
                x1, y1 = i, i + j
                x2, y2 = y1, n - i - 1
                x3, y3 = y2, n - i - 1 - j
                x4, y4 = y3, i
                a, b, c, d = matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4]
                matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4] = d, a, b, c

        i = 0
        n = len(matrix)
        cur_steps = n - 1
        while cur_steps > 0:
            rotate_points_on_cur_ring(i, cur_steps)
            i += 1
            cur_steps -= 2

        return


import copy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.set_init_para(matrix)
        n = len(matrix)
        cnt = 0 if n % 2 == 0 else 1

        while cnt < n * n:
            pts = self.get_cur_starting_points()
            steps = self.get_steps(pts)
            for _ in range(steps):
                self.swap_quad_vals(pts)
                self.move_to_next_quad(pts)
                cnt += 4

            self.update_starting_points()

    """
    the following functions can be ignored
    """

    def set_init_para(self, matrix):
        self.matrix = matrix
        self.matrix_size = len(matrix)
        n = self.matrix_size
        self.starting_points = [[0, 0], [0, n - 1], [n - 1, n - 1], [n - 1, 0]]
        self.updating_vectors = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        self.moving_vectors = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def get_cur_starting_points(self):
        pts = copy.deepcopy(self.starting_points)
        return pts

    def get_steps(self, pts):
        return pts[1][1] - pts[0][1]

    def update_starting_points(self):
        for i in range(4):
            self.starting_points[i][0] += self.updating_vectors[i][0]
            self.starting_points[i][1] += self.updating_vectors[i][1]

    def swap_quad_vals(self, pts):
        x1, y1 = pts[0]
        x2, y2 = pts[1]
        x3, y3 = pts[2]
        x4, y4 = pts[3]
        a, b, c, d = self.matrix[x1][y1], self.matrix[x2][y2], self.matrix[x3][y3], self.matrix[x4][y4]
        self.matrix[x1][y1], self.matrix[x2][y2], self.matrix[x3][y3], self.matrix[x4][y4] = d, a, b, c

    def move_to_next_quad(self, pts):
        for i in range(4):
            pts[i][0] += self.moving_vectors[i][0]
            pts[i][1] += self.moving_vectors[i][1]
