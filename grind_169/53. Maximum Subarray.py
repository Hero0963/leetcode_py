# ref = https://zh.wikipedia.org/zh-tw/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98

class Solution:
    """
    N = len(nums)
    time complexity: O(N)
    space complexity: O(1)

    Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

    """

    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = max_so_far = nums[0]

        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
