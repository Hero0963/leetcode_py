import collections
import bisect


# N: len(nums)
# M: max_len element in record
# TC: O(N + NlogM)
# SC: O(N)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        record = collections.defaultdict(list)
        prefix_sum = 0
        record[0].append(-1)
        res = 0
        for i, x in enumerate(nums):
            prefix_sum += x
            record[prefix_sum].append(i)

        for key, idx_list in record.items():
            dual_key = key - k
            if dual_key not in record:
                continue

            dual_idx_list = record[dual_key]
            # print("key, idx_list, dual_idx_list = ", key, idx_list, dual_idx_list)

            for idx in idx_list:
                rank = bisect.bisect_left(dual_idx_list, idx)
                res += rank

        return res


import collections


# N: len(nums)
# TC: O(N)
# SC: O(N)

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
