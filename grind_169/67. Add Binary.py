class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        ls = []
        q = 0
        i, j = m - 1, n - 1
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            q, r = divmod(x + y + q, 2)
            ls.append(str(r))
            i -= 1
            j -= 1

        if q != 0:
            ls.append(str(q))

        ans = "".join(reversed(ls))  # 使用reversed函數反轉列表

        return ans


# M: len(a)
# N: len(b)
# WOLG: let M <= N
# TC: O(N + N + N)
# SC: O(N)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 將二進制字符串轉換為整數
        int_a = int(a, 2)
        int_b = int(b, 2)

        # 將整數相加
        result_int = int_a + int_b

        # 將結果轉換為二進制字符串
        result_binary = bin(result_int)

        # 刪除開頭的'0b'前綴
        result_binary = result_binary[2:]

        return result_binary
