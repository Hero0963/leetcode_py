# N: n
# TC: O(2^N)
# SC: O(2^N)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.max_stack_cnt = 0

        def is_valid(s):
            stack = []
            for p in s:
                if not stack:
                    stack.append(p)
                    continue

                if p == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(p)

            if not stack:
                return True

            return False

        def helper(cur, ul, ur, stack_cnt):
            if ul == n and ur == n:
                self.max_stack_cnt = max(stack_cnt, self.max_stack_cnt)

                if is_valid(cur):
                    self.res.append(cur)

            if cur[-1] == "(":
                if ul != n:
                    helper(cur + "(", ul + 1, ur, stack_cnt + 1)

                if ur != n:
                    helper(cur + ")", ul, ur + 1, stack_cnt + 1)

            if cur[-1] == ")":
                if ul != n:
                    helper(cur + "(", ul + 1, ur, stack_cnt + 1)

                if ur != n:
                    helper(cur + ")", ul, ur + 1, stack_cnt + 1)

        helper("(", 1, 0, 1)

        # if self.max_stack_cnt > 2 ** n:
        #     print(self.max_stack_cnt)
        #     return []
        return self.res


# N: n
# TC: O(2^N)
# SC: O(2^N)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def helper(cur, ul, ur):
            if ul == n and ur == n:
                self.res.append(cur)
                return

            if ul < n:
                helper(cur + "(", ul + 1, ur)

            if ul > ur:
                helper(cur + ")", ul, ur + 1)

        helper("(", 1, 0)

        return self.res
