class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k + 1:
            return n

        ans = 0
        left = 0
        max_f = 0
        counter = [0] * 26
        for right, c in enumerate(s):
            i = ord(c) - ord("A")
            counter[i] += 1
            max_f = max(max_f, counter[i])

            cur_leng = right - left + 1
            while cur_leng > max_f + k:
                counter[ord(s[left]) - ord("A")] -= 1
                left += 1
                cur_leng -= 1

            if cur_leng > ans:
                ans = cur_leng

        return ans

# N: len(s)
# TC: O(N)
# SC: O(1)
# by @lee215, we can use max_f replace max(counter.values) and
# cur_leng is always valid when max_f + k >= cur_leng
