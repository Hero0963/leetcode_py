class Solution:
    def reverse(self, x: int) -> int:
        lower_bound = - 2 ** 31
        upper_bound = 2 ** 31 - 1

        sign = 1 if x >= 0 else -1
        x = abs(x)
        y = 0
        while x > 0:
            q, r = divmod(x, 10)
            y = y * 10 + r
            x = q
        y *= sign

        if y < lower_bound or y > upper_bound:
            y = 0

        return y

# TC: O(logx), here abs(x) < 2^32
# SC: O(1)
# we may check whether out of range by ((y-r)//10 )== prey
