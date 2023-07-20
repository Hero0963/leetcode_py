import collections


# N: len(s)
# M: number of distinct chars in s,
# s consists of lowercase/uppercase English letters only.
# so M < 26 +26
# TC: O(N + M) = O(N)
# SC: O(M) = O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        counter = collections.Counter(s)
        odd = 0
        for v in counter.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                odd = 1

        return res + odd
