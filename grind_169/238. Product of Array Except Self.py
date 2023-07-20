# N: len(nums)
# TC: O(N)
# SC: O(1), no extra memory

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        product = 1
        for i in range(n):
            res[i] = product
            product *= nums[i]

        product = 1
        for j in range(n - 1, - 1, - 1):
            res[j] *= product
            product *= nums[j]

        return res
