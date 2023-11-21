import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = collections.defaultdict(int)
        head = 0
        ans = 0
        for tail, char in enumerate(s):
            if char in record:
                head = max(head, record[char] + 1) # consider "cabbcdefg"
            record[char] = tail
            cur_length = tail - head + 1
            ans = max(ans, cur_length)

        return ans


# N: len(s)
# TC: O(N)
# SC: O(1), s consists of English letters, digits, symbols and spaces.