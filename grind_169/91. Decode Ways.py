class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if s[i] != "0":
                dp[i] += dp[i - 1]

            combined_val = int(s[i - 1] + s[i])
            if 10 <= combined_val <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1

        return dp[-1]

# N: len(s)
# TC: O(N)
# SC: O(N)
