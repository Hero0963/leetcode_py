from sortedcontainers import SortedDict


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left = 0
        sd = SortedDict()
        for right, x in enumerate(nums):
            if x in sd:
                sd[x] += 1
            else:
                sd[x] = 1

            if right < k - 1:
                continue

            while right - left + 1 > k:
                y = nums[left]
                sd[y] -= 1
                if sd[y] == 0:
                    del sd[y]
                left += 1

            ans.append(sd.peekitem(-1)[0])
        return ans

# N: len(nums)
# TC: O(N + NlogN)
# SC: O(N)
