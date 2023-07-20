from typing import List
from collections import defaultdict


class Solution:
    """
    n : len(nums)
    time complexity: O(N), one-pass nums
    space complexity: O(N), we use hash_map to save visited info

    Constraints:
    2 <= nums.length <= 10^4
    -10^6 <= nums[i] <= 10^9
    -10^9<= target <= 10^9
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for idx, n in enumerate(nums):
            if n in hash_map:
                return [idx, hash_map[n]]
            else:
                hash_map[target - n] = idx

        # If no pairs satisfy the condition
        return [-1, -1]
