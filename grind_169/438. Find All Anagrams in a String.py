import collections


# M: len(s)
# N: len(p)
# TC: O(M + N)
# SC: O(1), since s and p consist of lowercase English letters.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        record = collections.Counter(p)
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return ans
        for i in range(len_p):
            record[s[i]] -= 1
            if record[s[i]] == 0:
                del record[s[i]]

        head, tail = 0, len_p - 1
        while tail < len_s:
            # print(head, tail, record)
            if not record:
                ans.append(head)

            record[s[head]] += 1
            if record[s[head]] == 0:
                del record[s[head]]
            head += 1

            tail += 1
            if tail == len_s:
                break
            record[s[tail]] -= 1
            if record[s[tail]] == 0:
                del record[s[tail]]

        return ans


import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return ans

        record_p = collections.Counter(p)
        record_s = collections.Counter()
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
