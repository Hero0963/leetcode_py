class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x

        return res

# N: len(nums)
# TC: O(N)
# SC: O(1)
