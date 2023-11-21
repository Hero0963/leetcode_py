class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, lambda p: p[0] ** 2 + p[1] ** 2)


# N: len(points)
# K: k
# TC: O(NlogK)
# SC: O(K)
