import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        record = collections.defaultdict(int)

        # check rows:
        for _row in board:
            record.clear()
            for x in _row:
                if x == ".":
                    continue

                record[x] += 1
                if record[x] > 1:
                    return False

        # check columns:
        for j in range(m):
            record.clear()
            for i in range(n):
                x = board[i][j]
                if x == ".":
                    continue

                record[x] += 1
                if record[x] > 1:
                    return False

        # check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[i][j: j + 3], board[i + 1][j: j + 3], board[i + 2][j: j + 3]]
                if not self.isvalid_subbox(sub_box):
                    return False

        return True

    def isvalid_subbox(self, sub_box: List[List[str]]) -> bool:
        record = collections.defaultdict(int)
        for _row in sub_box:
            for x in _row:
                if x == ".":
                    continue

                record[x] += 1
                if record[x] > 1:
                    return False

        return True


# Since the Sudoku size is 9 x9, fixed here
# TC: O(1)
# SC: O(1)

# note if Sudoku size extend to be N * N
# TC: O(N * N)
# SC: O(N + N * N), can be reruced to be O(N)


from typing import List


class Solution:

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

# ref= https://leetcode.com/problems/valid-sudoku/discuss/1622505/Pythonic-Python
