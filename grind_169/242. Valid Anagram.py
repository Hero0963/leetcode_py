from collections import defaultdict


class Solution:
    """
    N : max(len(s) , len(t)), should be the same
    time complexity: O(N)
    space complexity: O(1), since s and t consist of lowercase English letters.

    Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

    we can also use count() function apply to set(s + t) or a~z

    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = defaultdict(int)
        for char_s in s:
            hash_map[char_s] += 1

        for char_t in t:
            hash_map[char_t] -= 1
            if hash_map[char_t] < 0:
                return False

        return True
