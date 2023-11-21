# N: len(s)
# TC: O(N)
# SC: O(N)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = "+"
        num = 0
        n = len(s)

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if i == n - 1 or c in "+-*/":
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    last_num = stack.pop() if stack else 1
                    stack.append(last_num * num)
                elif pre_op == "/":
                    last_num = stack.pop() if stack else 1
                    if last_num < 0:
                        stack.append(int(last_num / num))
                    else:
                        stack.append(last_num // num)
                pre_op = c
                num = 0
        return sum(stack)
