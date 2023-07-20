# M: len(a)
# N: len(b)
# TC: O(M+N)
# SC: O(1)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# M: len(a)
# N: len(b)
# R: max(M, N)
# TC: O(M+N)
# SC: O(R)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        res = ""
        q = 0
        i, j = m - 1, n - 1
        while i >= 0 or j >= 0:
            x, y = 0, 0
            if i >= 0:
                x = int(a[i])
            if j >= 0:
                y = int(b[j])

            q, r = divmod(x + y + q, 2)
            res += str(r)
            i -= 1
            j -= 1

        if q != 0:
            res += str(q)
        ans = res[::-1]
        return ans
