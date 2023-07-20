import collections


# N: len(nums)
# TC: O(N)
# SC: O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = collections.defaultdict(int)
        goal = len(nums) // 2
        for v in nums:
            seen[v] += 1
            if seen[v] > goal:
                return v

        return -1


# https://ithelp.ithome.com.tw/articles/10245248
# Boyer–Moore majority vote algorithm
# N: len(nums)
# TC: O(N)
# SC: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        goal = len(nums) // 2
        cur_val, cur_max = -1, 1
        for v in nums:
            if v == cur_val:
                cur_max += 1
            else:
                cur_max -= 1

            if cur_max > goal:
                return cur_val

            if cur_max == 0:
                cur_val, cur_max = v, 1

        return cur_val
