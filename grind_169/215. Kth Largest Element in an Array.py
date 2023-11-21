import heapq


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


# N: len(nums)
# TC: O(N + KlogN)
# SC: O(N)


from sortedcontainers import SortedList


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sd = SortedList(key=lambda x: -x)
        for x in nums:
            sd.add(x)
            if len(sd) > k:
                sd.pop()

        return sd[-1]

# N: len(nums)
# TC: O(N + KlogN)
# SC: O(K)
