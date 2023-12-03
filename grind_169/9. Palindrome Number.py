class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)
        head = 0
        tail = len(str_x) - 1

        while head < tail:
            if str_x[head] != str_x[tail]:
                return False
            head += 1
            tail -= 1

        return True


# N: x
# TC: O(logN)
# SC: O(logN)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        if x % 10 == 0:
            return False

        rev = 0
        r = 0

        while rev < x:
            r = x % 10
            rev = rev * 10 + r
            x = x // 10

        if (x == rev) or (x == rev // 10):
            return True

        return False

# N: x
# TC: O(logN)
# SC: O(logN)
