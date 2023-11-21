class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)
        start, end, max_leng = 0, 0, 0

        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            max_leng = 1
            ans = s[i]

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_leng = 2
                ans = s[i: i + 1 + 1]

        for j in range(n):
            for i in range(0, j - 1):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    cur_leng = j - i + 1
                    if max_leng < cur_leng:
                        ans = s[i: j + 1]
                        max_leng = cur_leng

        return ans

# N: len(s)
# TC: O(N^2)
# SC: O(N^2)
# key : if s[i] == s[j] and dp[i + 1][j - 1]:
