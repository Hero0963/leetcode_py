class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        check = 0
        while True:
            slow = nums[slow]
            check = nums[check]
            if slow == check:
                break

        return check

# ref = https://leetcode.com/problems/find-the-duplicate-number/solutions/515872/python-js-java-go-c-o-1-aux-space-by-hopping-w-hint/
# N: len(nums)
# TC: O(N)
# SC: O(1)
