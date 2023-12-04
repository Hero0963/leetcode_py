class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        missing_number = n + 1
        for i in range(n):
            while True:
                x = nums[i]
                if 1 <= x <= n and x != nums[x - 1]:
                    nums[x - 1], nums[i] = nums[i], nums[x - 1]
                else:
                    break

        for i in range(n):
            if i + 1 != nums[i]:
                missing_number = i + 1
                break

        return missing_number

# N: len(nums)
# TC: O(N)
# SC: O(1), in-place
# we want nums be arranged to the form: if x \in [1, n], then nums[x-1] = x
# so we put x to the pos (x - 1).
