import collections


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = collections.defaultdict(int)
        for idx, x in enumerate(nums):
            y = target - x
            if y in seen:
                return [idx, seen[y]]
            else:
                seen[x] = idx


        not_exist = [-1, -1]
        return not_exist


# N: len(nums)
# TC: O(N)
# SC: O(N)
