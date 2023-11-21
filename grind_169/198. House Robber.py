class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        pre_pre, pre, cur = nums[0], max(nums[0], nums[1]), max(nums[0], nums[1])
        for i in range(2, n):
            cur = max(pre, pre_pre + nums[i])
            pre_pre, pre = pre, cur

        return cur

# N: len(nums)
# TC: O(N)
# SC: O(1)
