class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, leng_word = len(board), len(board[0]), len(word)

        def dfs(r, c, l):
            if l == leng_word:
                return True

            if not (0 <= r < n and 0 <= c < m):
                return False

            if board[r][c] != word[l]:
                return False

            ori_char = board[r][c]
            board[r][c] = "#"

            flag = dfs(r + 1, c, l + 1) or dfs(r - 1, c, l + 1) or dfs(r, c + 1, l + 1) or dfs(r, c - 1, l + 1)

            board[r][c] = ori_char
            return flag

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False

# N: len(board)
# M: len(board[0])
# L: len(word)

# TC: O(M * N * 3^(L-1))
# SC: O(L)
