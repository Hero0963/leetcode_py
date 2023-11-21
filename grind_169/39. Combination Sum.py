class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.dfs(candidates, target, 0, [])
        return self.ans

    def dfs(self, nums: List[int], rem: int, idx: int, pick: List[int]):
        if rem == 0:
            self.ans.append(pick)
            return

        for i in range(idx, len(nums)):
            val = nums[i]
            if val > rem:
                return
            else:
                self.dfs(nums, rem - nums[i], i, pick + [val])

# N: len(candidates)
# T: target
# TC: O(NlogN + N * 2^N )
# SC: O(T), excluding ans
# complexity analysis check: https://leetcode.cn/problems/combination-sum/solutions/406516/zu-he-zong-he-by-leetcode-solution/
