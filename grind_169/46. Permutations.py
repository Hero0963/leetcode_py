import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.ans = []
        path = [0 for _ in range(n)]
        is_used = [False for _ in range(n)]

        def dfs(i: int):
            if i == n:
                self.ans.append(copy.deepcopy(path))
                return

            for j in range(n):
                if not is_used[j]:
                    path[i] = nums[j]
                    is_used[j] = True
                    dfs(i + 1)
                    is_used[j] = False

        dfs(0)
        return self.ans

# N: len(nums)
# TC: O(N x N!)
# SC: O(N!), if consider ans, else O(N)
