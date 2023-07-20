from typing import List


class Solution:
    """
    N : len(nums)
    time complexity: O(logN)
    space complexity: O(1)

    Constraints:

    1 <= nums.length <= 10^4
    -10^4 < nums[i], target < 10^4
    All the integers in nums are unique.
    nums is sorted in ascending order.

    """

    def search(self, nums: List[int], target: int) -> int:
        head, tail = 0, len(nums) - 1

        while head <= tail:
            mid = head + (tail - head) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid - 1
            else:
                head = mid + 1

        return -1
