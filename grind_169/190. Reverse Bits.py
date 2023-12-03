class Solution:
    def reverseBits(self, n: int) -> int:
        input_length = 32
        res = 0
        cnt = 0
        while cnt < input_length:
            r = n % 2
            res = res * 2 + r
            n = n // 2
            cnt += 1
        return res

# N: input_length, here N = 32 is fixed.
# TC: O(1)
# SC: O(1)
