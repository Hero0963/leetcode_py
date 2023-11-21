import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        m, n = len(s), len(t)
        need = collections.Counter(t)
        head, cnt = 0, 0
        for tail, c in enumerate(s):
            need[c] -= 1
            if need[c] >= 0:
                cnt += 1
            while cnt == n:
                if not ans or len(ans) > tail - head + 1:
                    ans = s[head: tail + 1]

                need[s[head]] += 1
                if need[s[head]] > 0:
                    cnt -= 1
                head += 1

        return ans

# M, N: len(s), len(t)
# C: size of char set
# TC: O(N + M)
# SC: O(C)
# note:
# s and t consist of uppercase and lowercase English letters. => here C = 26 + 26
# The testcases will be generated such that the answer is unique.
