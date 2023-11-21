from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_count  = defaultdict(int)
        for c in s:
            letter_count [c] += 1

        for c in t:
            letter_count [c] -= 1
            if letter_count [c] < 0:
                return False

        return True


# S: len(s)
# T: len(t)
# TC: O(S + T)
# SC: O(26), since s and t consist of lowercase English letters.