# N: len(intervals)
# TC: O(N)
# SC: O(N)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda s: s[0])
        pre = intervals[0]
        ans = []

        for cur in intervals:
            if cur[0] > pre[1]:
                ans.append(pre)
                pre = cur
            else:
                pre = [pre[0], max(pre[1], cur[1])]

        ans.append(pre)
        return ans
