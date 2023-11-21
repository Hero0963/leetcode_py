# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        head, tail = 1, n
        while head <= tail:
            mid = head + (tail - head)//2
            if isBadVersion(mid):
                tail = mid - 1
            else:
                head = mid + 1
        return head


# N: n
# C: time complexity for isBadVersion(version: int) -> bool:
# TC: O(logN*C)
# SC: O(1)