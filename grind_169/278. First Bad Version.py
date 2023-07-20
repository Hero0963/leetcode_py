# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    """
    N = n
    time complexity: O(logN)
    space complexity: O(1)

    Constraints:
    1 <= bad <= n <= 2^31 - 1
    """

    def firstBadVersion(self, n: int) -> int:
        head, tail = 0, n - 1
        while head <= tail:
            mid = head + (tail - head) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    tail = mid - 1

            else:
                head = mid + 1

        return head
