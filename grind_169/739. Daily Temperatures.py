class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i, t))
                continue

            while stack:
                pre_i, pre_t = stack[-1]
                if pre_t < t:
                    ans[pre_i] = i - pre_i
                    stack.pop()
                else:
                    break

            stack.append((i, t))

        return ans

# N: len(temperatures)
# TC: O(N)
# SC: O(N)
