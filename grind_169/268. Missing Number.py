# N: len(nums)
# TC: O(N)
# SC: O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for idx, val in enumerate(nums):
            res = res + idx - val

        return res
