import collections


# ref = https://www.twblogs.net/a/5bb51cc62b71770e645e57e5
# M, N = len(s), len(t)
# TC: O(M+N)
# SC: O(1), since s and t consist of uppercase and lowercase English letters.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        m, n = len(s), len(t)
        head, cnt, cur_leng = 0, 0, m + 1
        need = collections.Counter(t)
        for tail, c in enumerate(s):
            need[c] -= 1
            if need[c] >= 0:
                cnt += 1
            while cnt == n:
                if cur_leng > tail - head + 1:
                    cur_leng = tail - head + 1
                    ans = s[head: tail + 1]
                need[s[head]] += 1
                if need[s[head]] > 0:
                    cnt -= 1
                head += 1

        return ans
