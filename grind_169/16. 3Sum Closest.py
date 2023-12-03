class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = math.inf
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                diff = abs(_sum - target)
                if diff < abs(ans - target):
                    ans = _sum
                if _sum == target:
                    return target
                elif _sum > target:
                    k -= 1
                else:
                    j += 1
        return ans

# N: len(nums)
# TC: O(NlogN + N^2)
# SC: O(N) for TimSort
