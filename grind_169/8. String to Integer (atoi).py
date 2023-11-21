class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        sign = 1
        num = 0
        ans = 0

        i = 0
        while i < n and s[i] == " ":
            i += 1  # skipping leading white space

        if i >= n:
            return 0

        if s[i] == "+" or s[i] == "-":
            if s[i] == "-":
                sign = -1

            i += 1

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # print(sign, num)
        ans = sign * num

        ans = min(ans, 2 ** 31 - 1)
        ans = max(ans, -(2 ** 31))
        return ans


# N: len(s)
# TC: O(N)
# SC: O(1)


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        ans = re.findall(r"^[+-]?\d+", s)
        # the pattern is ^[+-]?\d+ which means that it will match any string
        # that starts with an optional sign (+/-) followed by one or more digits.
        if not ans:
            return 0

        ans = int(ans[0])
        ans = min(ans, 2 ** 31 - 1)
        ans = max(ans, -(2 ** 31))

        return ans

# N: len(s)
# TC: O(N)
# SC: O(N)
# the pattern is ^[+-]?\d+ which means that it will match any string
# that starts with an optional sign (+/-) followed by one or more digits.
