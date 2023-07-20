# variant of #53. Maximum Subarray, Kadane's algorithm
# N: len(nums)
# TC: O(N)
# SC: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cur_max = cur_min = ans = nums[0]
        for i, v in enumerate(nums):
            if i == 0:
                continue

            pre_max, pre_min = cur_max, cur_min
            cur_max = max(pre_max * v, pre_min * v, v)
            cur_min = min(pre_max * v, pre_min * v, v)
            ans = max(ans, cur_max)

        return ans
