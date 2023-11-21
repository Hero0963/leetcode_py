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


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        goal = len(nums) // 2
        candidate, count = 0, 1
        for v in nums:
            if v == candidate:
                count += 1
            else:
                count -= 1

            if count > goal:
                return candidate

            if count == 0:
                candidate, count = v, 1

        return candidate

# N: len(nums)
# TC: O(N)
# SC: O(1)
# https://ithelp.ithome.com.tw/articles/10245248
# Boyer–Moore majority vote algorithm
