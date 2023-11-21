# N: len(intervals)
# TC: O(NlogN)
# SC: O(N)

# sort by starting points: the minimum number of intervals to cover the whole range
# sort by ending points: the maximum number of intervals that are non-overlapping

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans, end = 0, -math.inf

        sorted_intervals = sorted(intervals, key=lambda v: v[1])
        for s, e in sorted_intervals:
            if s >= end:
                end = e
            else:
                ans += 1

        return ans
