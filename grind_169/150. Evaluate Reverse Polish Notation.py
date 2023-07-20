# N: len(token)
# TC :O(N)
# SC: O(N), stacks to store  t in token
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operators = "+-*/"
        stacks = []
        for t in tokens:
            if t not in valid_operators:
                stacks.append(int(t))
                continue

            n2 = stacks.pop()
            n1 = stacks.pop()
            res = -1
            match t:
                case "+":
                    res = n1 + n2
                case "-":
                    res = n1 - n2
                case "*":
                    res = n1 * n2
                case "/":
                    res = int(n1 / n2)
                case _:
                    pass

            stacks.append(res)

        return stacks[-1]
