# N: len(s)
# TC: O(N)
# SC: O(1), since s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hash_map = {}
        head = 0

        for tail, char in enumerate(s):
            if char in hash_map:
                # @srockets commented, consider "cabbcdefg"
                head = max(head, hash_map[char] + 1)
            hash_map[char] = tail
            cur_length = tail - head + 1
            ans = max(ans, cur_length)

        return ans
