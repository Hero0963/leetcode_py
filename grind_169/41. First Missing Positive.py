# N: len(nums)
# TC: O(N)
# SC: O(1), in-place

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        missing_number = n + 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                missing_number = i + 1
                break

        return missing_number
