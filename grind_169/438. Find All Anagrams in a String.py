import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return ans

        record_s = collections.Counter()
        record_p = collections.Counter(p)

        for i in range(len_p):
            record_s[s[i]] += 1

        head, tail = 0, len_p - 1
        while tail < len_s:
            if record_s == record_p:
                ans.append(head)

            record_s[s[head]] -= 1
            head += 1

            tail += 1
            if tail >= len_s:
                break
            record_s[s[tail]] += 1

        return ans

# S: len(s)
# P: len(P)
# TC: O(P + S *26)
# SC: O(26), since s and p consist of lowercase English letters.
