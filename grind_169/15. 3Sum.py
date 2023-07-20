
# N : len(nums)
# TC: O(NlogN + N^2)
# SC: O(N), list(res_set) as return

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    res_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif _sum > 0:
                    k -= 1
                else:
                    j += 1

        return list(res_set)