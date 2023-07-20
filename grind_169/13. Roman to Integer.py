import collections
import math


# N: len(s)
# TC: O(N)
# SC: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = collections.defaultdict(int)
        hash_map["I"] = 1
        hash_map["V"] = 5
        hash_map["X"] = 10
        hash_map["L"] = 50
        hash_map["C"] = 100
        hash_map["D"] = 500
        hash_map["M"] = 1000

        ans = 0
        pre_val = math.inf
        for x in s:
            val = hash_map[x]
            if pre_val >= val:
                ans += val
                pre_val = val
            else:
                ans -= pre_val
                ans += val - pre_val
                pre_val = val

        return ans
