# ref = https://www.youtube.com/watch?v=FTrEHdKJzpc

# N: len(nums)
# M: target = _sum // 2
# TC: O(MN)
# SC: O(MN)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False

        n = len(nums)
        target = _sum // 2
        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(target + 1):
                # print(i, j)
                dp[i][j] = dp[i - 1][j]

                if nums[i] == j:
                    dp[i][j] = True
                elif nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

                if dp[i][target]:
                    return True

        return dp[-1][-1]
