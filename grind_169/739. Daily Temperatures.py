# N: len(temperatures)
# TC: O(N + N) , at most traverse twice (temperatures + stack)
# SC: O(N)

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


"""
other solutions:
sol II. hash_map[T] = [d1, d2, d3,...]
sol III. monotonic stack record an increasing [(i1, t1), (i2, t2), ...]
for j in range(n), binary search the monotonic stack to find  next higher i, t
"""
