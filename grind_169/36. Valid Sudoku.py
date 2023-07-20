import collections


# Since the Sudoku size is 9 x9, fixed here
# TC: O(1)
# SC: O(1)

# note if Sudoku size extend to be N * N
# TC: O(N * N)
# SC: O(N + N * N), can be reruced to be O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        hash_map = collections.defaultdict(int)

        # check rows:
        for _row in board:
            hash_map.clear()
            for x in _row:
                if x == ".":
                    continue

                hash_map[x] += 1
                if hash_map[x] > 1:
                    return False

        # check columns:
        for j in range(m):
            hash_map.clear()
            for i in range(n):
                x = board[i][j]
                if x == ".":
                    continue

                hash_map[x] += 1
                if hash_map[x] > 1:
                    return False

        # check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[i][j: j + 3], board[i + 1][j: j + 3], board[i + 2][j: j + 3]]
                if not self.isvalid_subbox(sub_box):
                    return False

        return True

    def isvalid_subbox(self, sub_box: List[List[str]]) -> bool:
        hash_map = collections.defaultdict(int)
        for _row in sub_box:
            for x in _row:
                if x == ".":
                    continue

                hash_map[x] += 1
                if hash_map[x] > 1:
                    return False

        return True



from typing import List


# ref= https://leetcode.com/problems/valid-sudoku/discuss/1622505/Pythonic-Python

class Solution:
    """
    N: len(board)=len(board[0])
    time complexity: O(N^2)
    space complexity: O(N^2)

    in this case, N = 9 is fixed.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = {i: [] for i in range(9)}
        check_col = {i: [] for i in range(9)}
        check_box = {i: [] for i in range(9)}

        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e == ".":
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if e in check_row[i] or e in check_col[j] or e in check_box[box_index]:
                    return False
                else:
                    check_row[i].append(e)
                    check_col[j].append(e)
                    check_box[box_index].append(e)

        return True