# N: len(s)
# TC: O(N)
# SC: O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k + 1:
            return n

        res = 0
        head = 0
        counter = [0] * 26
        for idx, c in enumerate(s):
            counter[ord(c) - ord("A")] += 1

            cur_leng = idx - head + 1
            while max(counter) + k < cur_leng:
                counter[ord(s[head]) - ord("A")] -= 1
                head += 1
                cur_leng = idx - head + 1

            res = max(res, cur_leng)

        return res


# N: len(s)
# TC: O(N)
# SC: O(1)
# by @lee215, we can use max_f replace max(counter.values) and
# cur_leng is always valid when max_f + k >= cur_leng

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k + 1:
            return n

        res = 0
        head = 0
        max_f = 0
        counter = [0] * 26
        for idx, c in enumerate(s):
            j = ord(c) - ord("A")
            counter[j] += 1
            max_f = max(max_f, counter[j])

            cur_leng = idx - head + 1
            if cur_leng > max_f + k:
                counter[ord(s[head]) - ord("A")] -= 1
                head += 1
                cur_leng = idx - head + 1

            res = max(res, cur_leng)

        return res
