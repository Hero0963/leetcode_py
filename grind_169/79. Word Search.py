# ref = https://fuxuemingzhu.cn/leetcode/79.html
# N: len(board)
# M: len(board[0])
# L: len(word)
# TC: O(NM*3^L), each element as starting point, at most walk L steps and each step has 3 diection choices
# SC: O(L)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        n, m, l_goal = len(board), len(board[0]), len(word)

        def helper(r, c, l):
            if l == l_goal:
                return True

            if r < 0 or r >= n or c < 0 or c >= m:
                return False

            if board[r][c] != word[l]:
                return False

            board[r][c], initial_char = "#", board[r][c]
            flag = helper(r + 1, c, l + 1) or helper(r - 1, c, l + 1) or helper(r, c + 1, l + 1) or helper(r, c - 1,
                                                                                                           l + 1)

            board[r][c] = initial_char
            return flag

        for i in range(n):
            for j in range(m):
                if helper(i, j, 0):
                    return True

        return False
