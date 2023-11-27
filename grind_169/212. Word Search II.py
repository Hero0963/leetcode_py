import collections


class MyTrie:
    def __init__(self):
        self.children = collections.defaultdict(MyTrie)
        self.word = ""

    def insert(self, word):
        node = self
        for c in word:
            node = node.children[c]

        node.is_word = True
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n, ans = len(board), len(board[0]), []
        trie = MyTrie()
        for word in words:
            trie.insert(word)

        def dfs(node, x, y):
            if board[x][y] not in node.children:
                return

            ch = board[x][y]

            nxt = node.children[ch]
            if nxt.word != "":
                ans.append(nxt.word)
                nxt.word = ""

            if nxt.children:
                board[x][y] = "*"
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n:
                        dfs(nxt, nx, ny)
                board[x][y] = ch

            if not nxt.children:
                node.children.pop(ch)

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return ans

# M: len(board)
# N: len(board[0])
# L len(words)
# K: max_leng of word in words
# TC: (M * N * 3 ^ (K - 1))
# SC: O(L * K)
# ref: https://leetcode.cn/problems/word-search-ii/solution/dan-ci-sou-suo-ii-by-leetcode-solution-7494/
