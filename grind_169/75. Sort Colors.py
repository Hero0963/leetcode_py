class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        color_red, color_white, color_blue = 0, 1, 2
        flag_red, flag_blue = 0, len(nums) - 1

        idx = 0
        while idx <= flag_blue:
            if nums[idx] == color_red:
                nums[flag_red], nums[idx] = nums[idx], nums[flag_red]
                idx += 1
                flag_red += 1
            elif nums[idx] == color_white:
                idx += 1
            elif nums[idx] == color_blue:
                nums[idx], nums[flag_blue] = nums[flag_blue], nums[idx]
                flag_blue -= 1


# N: len(nums)
# TC: O(N)
# SC: O(1)

import collections


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = collections.Counter(nums)
        # print(counter)
        pos = 0
        for color in range(3):
            val = counter[color]
            while val > 0:
                nums[pos] = color
                pos += 1
                val -= 1

# N: len(nums)
# TC: O(N)
# SC: O(N)
