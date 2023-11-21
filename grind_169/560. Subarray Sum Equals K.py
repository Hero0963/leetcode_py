import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        record = collections.defaultdict(int)
        pre_sum = 0
        record[0] += 1
        ans = 0

        for x in nums:
            pre_sum += x
            dual_sum = pre_sum - k
            if dual_sum in record:
                ans += record[dual_sum]

            record[pre_sum] += 1

        return ans

# N: len(nums)
# TC: O(N)
# SC: O(N)
