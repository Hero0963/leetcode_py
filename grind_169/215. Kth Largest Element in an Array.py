import heapq


# N: len(nums)
# TC: O(N + KlogN)
# SC: O(N)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-x for x in nums]
        heapq.heapify(h)

        res = h[-1]
        for i in range(k):
            if i == k - 1:
                res = -heapq.heappop(h)
            else:
                heapq.heappop(h)

        return res
