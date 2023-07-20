import collections


# N: len(nums)
# TC: O(N)
# SC: O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))

        seen = collections.defaultdict(bool)
        for num in nums:
            if num in seen:
                return True
            seen[num] = True

        return False
