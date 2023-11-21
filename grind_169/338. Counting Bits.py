class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = 1 + dp[(i - 1) // 2]

        return dp

# N: n
# TC: O(N)
# SC: O(N)
# consider *2 in binary representation means shift
# for i = odd case, it equals to previous one (i - 1) binary form + 1
# Brian Kernighan's algorithm is also helpful
