# ref= https://blog.csdn.net/fuxuemingzhu/article/details/79368360

from typing import List


# N: len(s)
# M: len(wordDict)
# TC: O(M^2)
# SC: O(M + N)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        word_set = set(wordDict)

        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]
