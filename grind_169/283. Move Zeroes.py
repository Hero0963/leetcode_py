# N: len(nums)
# TC: O(N)
# SC: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zero_idx = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[non_zero_idx] = nums[non_zero_idx], nums[i]
                non_zero_idx += 1
