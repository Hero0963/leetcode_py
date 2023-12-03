class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target + 1)]
        for i in range(len(dp)):
            for num in nums:
                if num > i:
                    break

                if num == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - num]

        return dp[-1]

# N: len(nums)
# T: target
# TC: O(NlogN + T * N)
# SC: O(T + N), O(N) for TimSort
