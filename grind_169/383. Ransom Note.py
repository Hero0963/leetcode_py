import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = collections.Counter(magazine)
        for r in ransomNote:
            counter[r] -= 1

        for v in counter.values():
            if v < 0:
                return False

        return True


# R: len(ransomNote)
# M: len(magazine)
# TC: O(N + M + 26)
# SC: O(26), since ransomNote and magazine consist of lowercase English letters.
