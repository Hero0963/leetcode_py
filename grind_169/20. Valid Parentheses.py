import collections


class Solution:
    def isValid(self, s: str) -> bool:
        dual_map = collections.defaultdict(str)
        dual_map[")"] = "("
        dual_map["}"] = "{"
        dual_map["]"] = "["

        stack = []
        for x in s:
            if x in dual_map:
                if not stack:
                    return False
                y = stack.pop()
                if dual_map[x] != y:
                    return False
            else:
                stack.append(x)

        return False if stack else True


# N: len(s)
# TC: O(N)
# SC: O(N)