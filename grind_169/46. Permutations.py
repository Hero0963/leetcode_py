# N: len(nums)
# TC: O(N!)
# SC: O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        visited = [False] * n

        def dfs(path):
            if len(path) == n:
                ans.append(path)
                return

            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    dfs(path + [nums[i]])
                    visited[i] = False

        dfs([])
        return ans
