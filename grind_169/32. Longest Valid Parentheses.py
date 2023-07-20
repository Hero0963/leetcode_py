# N: len(s)
# TC: O(N)
# SC: O(1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        left, right = 0, 0
        for p in s:
            if p == "(":
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, left + right)
            elif right > left:
                left, right = 0, 0

        n = len(s)
        left, right = 0, 0
        for i in range(n - 1, -1, -1):
            p = s[i]
            if p == ")":
                right += 1
            else:
                left += 1

            if right == left:
                ans = max(ans, left + right)
            elif left > right:
                left, right = 0, 0

        return ans
