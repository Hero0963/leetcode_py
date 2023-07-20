"""
there are so many methods to solve the problem, according to the requirements:
SC = O(1), TC = O(N)
V 2 pointers solutions
binary search
index sorting
hash_map
bit manipulation
"""


# ref = https://leetcode.com/problems/find-the-duplicate-number/solutions/515872/python-js-java-go-c-o-1-aux-space-by-hopping-w-hint/

# N: len(nums)
# TC: O(N)
# SC: O(1)

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


# N: len(nums)
# TC: O(logN * N)
# SC: O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        head, tail = 1, len(nums)

        def check(val):
            cnt = 0
            for x in nums:
                if x <= val:
                    cnt += 1
            return cnt

        while head < tail:
            mid = head + (tail - head) // 2
            cnt = check(mid)

            # exclude [head, mid] interval
            if cnt <= mid:
                head = mid + 1

            # duplicate number in [head, tail] interval
            else:
                tail = mid

        return head
