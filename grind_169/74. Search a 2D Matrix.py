class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def convert_number_to_matrix_pos(number) -> Tuple[int]:
            x, y = divmod(number, n)
            return (x, y)

        head, tail = 0, m * n - 1
        while head <= tail:
            mid = head + (tail - head) // 2
            i, j = convert_number_to_matrix_pos(mid)
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                head = mid + 1
            else:
                tail = mid - 1

        return False

# M: len(matrix)
# N: len(matrix[0])
# TC: O(MN)
# SC: O(1)
