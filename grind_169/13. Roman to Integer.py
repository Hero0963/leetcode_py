import collections
import math


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_2_int = collections.defaultdict(int)
        roman_2_int["I"] = 1
        roman_2_int["V"] = 5
        roman_2_int["X"] = 10
        roman_2_int["L"] = 50
        roman_2_int["C"] = 100
        roman_2_int["D"] = 500
        roman_2_int["M"] = 1000

        ans = 0
        pre_val = math.inf
        for c in s:
            val = roman_2_int[c]
            if pre_val >= val:
                ans += val
            else:
                ans -= pre_val
                ans += val - pre_val

            pre_val = val

        return ans

# N: len(s)
# TC: O(N)
# SC: O(1)
