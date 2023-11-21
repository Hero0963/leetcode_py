import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        even_count = 0
        odd_count = 0
        for v in counter.values():
            if v % 2 == 0:
                even_count += v
            else:
                even_count += v - 1
                odd_count = 1

        return even_count + odd_count

# N: len(s)
# TC: O(N)
# SC: O(1), since s consists of lowercase and/or uppercase English letters only.
