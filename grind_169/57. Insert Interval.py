class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif  newInterval[1] < interval[0]:
                res.append(newInterval)
                newInterval = interval
            else:
                newInterval = [min(interval[0],newInterval[0]), max(interval[1],newInterval[1])]

        res.append(newInterval)
        return res

# N: len(intervals)
# TC: O(N)
# SC: O(1)
# we may also use binary search to find the insert pos, ref = https://leetcode.com/problems/insert-interval/solutions/1444764/python-binary-search/

