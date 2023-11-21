class Solution:
    def calculate(self, s: str) -> int:
        ans, num, sign = 0, 0, 1
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                ans = ans + sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif c == ")":
                ans = ans + sign * num
                num = 0
                ans *= stack.pop()
                ans += stack.pop()

        ans = ans + sign * num
        return ans

# N: len(s)
# TC: O(N)
# SC: O(N)
