class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum, cur_sum = -math.inf, 0
        for x in nums:
            cur_sum = max(x, cur_sum + x)
            best_sum = max(best_sum, cur_sum)
        return best_sum


# Kadane's algorithm, https://en.wikipedia.org/wiki/Maximum_subarray_problem
# N: len(nums)
# TC: O(N)
# SC: O(1)