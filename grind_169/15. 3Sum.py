class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        record = set()
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break

            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    record.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif _sum > 0:
                    k -= 1
                else:
                    j += 1

        return list(record)

# N: len(nums)
# TC: O(N^2 + NlogN)
# SC: O(N)
