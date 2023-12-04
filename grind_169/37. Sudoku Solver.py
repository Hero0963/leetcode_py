class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(row: int, col: int, ch: str) -> bool:
            for i in range(9):
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch:
                    return False

            return True

        size = 9
        candidates = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

        def solve(row: int, col: int) -> bool:
            if row == size:
                return True
            if col == size:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                for c in candidates:
                    if is_valid(row, col, c):
                        board[row][col] = c

                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."

                return False
            else:
                return solve(row, col + 1)

        _ = solve(0, 0)
        return

# N: unsolved_cnt
# TC: O(9^N)
# SC: O(N)
