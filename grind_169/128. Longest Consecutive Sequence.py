class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 1
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue

            x = num
            while x in nums_set:
                x += 1

            _leng = x - num
            ans = max(ans, _leng)

        return ans

# N: len(nums)
# TC: O(N)
# SC: O(N)
