# N: len(nums)
# TC: O(N)
# SC: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach or max_reach >= n - 1:
                break

            max_reach = max(max_reach, i + nums[i])

        return max_reach >= n - 1


# N: len(nums)
# TC: O(N)
# SC: O(N)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = max(dp[i - 1], nums[i - 1]) - 1
            if dp[i] < 0:
                return False

        return True
