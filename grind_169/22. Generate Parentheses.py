class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs(left=n, right=n, path="")
        return self.res

    def dfs(self, left: int, right: int, path: str) -> None:
        if left == 0 and right == 0:
            self.res.append(path)
            return

        if left > 0:
            self.dfs(left - 1, right, path + "(")
        if left < right:
            self.dfs(left, right - 1, path + ")")

# N: n
# TC: O(4^N/N^(1/2))
# SC: O(4^N/N^(1/2)), can be reduced by backtracking

# ref = https://leetcode.cn/problems/generate-parentheses/solutions/194208/ru-men-ji-bie-de-hui-su-fa-xue-hui-tao-lu-miao-don/

# https://leetcode.cn/problems/generate-parentheses/solutions/192912/gua-hao-sheng-cheng-by-leetcode-solution/
