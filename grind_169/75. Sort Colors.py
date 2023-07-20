import collections


# N: len(nums)
# TC: O(N)
# SC: O(N)
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

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two = 0, len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] =nums[two], nums[i]
                two -= 1
