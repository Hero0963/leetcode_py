class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)

        return False

# N: len(nums)
# TC: O(N)
# SC: O(N)
