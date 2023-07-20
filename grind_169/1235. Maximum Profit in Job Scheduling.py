# whenever we encounter non-overlapping interval type problem, we may ort by endTime
# ref = https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/409009/JavaC++Python-DP-Solution/


# N: len(startTime)
# TC: O(NlogN)
# SC: O(N)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect_left(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])

        # n = len(startTime)
        # print("n, dp = ", n, dp)

        return dp[-1][1]
