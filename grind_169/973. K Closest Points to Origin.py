class Solution:
    """
    N = len(points), K = k
    time complexity: O(NlogK)
    space complexity: O(K) , need to return

    Constraints:
    1 <= k <= points.length <= 10^4
    -10^4 < xi, yi < 10^4
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, lambda p: p[0] ** 2 + p[1] ** 2)

        # # another O(NlogN) solution
        # points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        # return points[:k]
