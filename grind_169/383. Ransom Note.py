import collections

# N = len(ransomNote), M = len(magazine)
# TC: O(N + M + 26) = O(N + M)
# SC: O(26) = O(1), since ransomNote and magazine consist of lowercase English letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = collections.defaultdict(int)

        for r in ransomNote:
            hash_map[r] += 1

        for m in magazine:
            hash_map[m] -= 1

        for v in hash_map.values():
            if v > 0:
                return False

        return True
