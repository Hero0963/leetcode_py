import collections


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        record = collections.defaultdict(int)
        record[0] = -1

        prefix_diff = 0
        for i, x in enumerate(nums):
            if x == 1:
                prefix_diff += 1
            else:
                prefix_diff -= 1

            if prefix_diff in record:
                ans = max(ans, i - record[prefix_diff])
            else:
                record[prefix_diff] = i

        return ans

# N: len(nums)
# TC: O(N)
# SC: O(N)
