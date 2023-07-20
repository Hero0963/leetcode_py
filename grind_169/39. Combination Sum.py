# N: len(candidates)
# M: val of target
# TC: O(N^M)
# SC: O(M^2)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.dfs(candidates, target, 0, [])
        return self.ans

    def dfs(self, nums, target, index, path):
        if target == 0:
            self.ans.append(path)
            return

        for i in range(index, len(nums)):
            if nums[i] > target:
                return

            self.dfs(nums, target - nums[i], i, path + [nums[i]])
