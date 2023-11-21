class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))  # 按照结束时间排序
        f = [0] * (len(jobs) + 1)
        for i, (_, st, p) in enumerate(jobs):
            j = bisect_right(jobs, (st, inf), hi=i)  # hi=i 表示二分上界为 i（默认为 n）
            f[i + 1] = max(f[i], f[j] + p)  # 为什么是 j 不是 j+1：上面算的是 > st，-1 后得到 <= st，但由于还要 +1，抵消了
        return f[-1]

# N: len(startTime)
# TC: O(NlogN)
# SC: O(N)
# ref = https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1913089/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/
# key:
# 不选第 i个工作：f[i]=f[i−1]
# 选第 i 个工作：f[i]=f[j]+profit[i]
# 其中 j 是最大的满足 endTime[j]≤startTime[i] 的 j，不存在时为 −1。
