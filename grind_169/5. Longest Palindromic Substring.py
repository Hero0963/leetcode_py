# N: len(s)
# TC: O(N^2)
# SC: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)

        # odd
        for i in range(n):
            head, tail = i, i
            while head >= 0 and tail < n:
                if s[head] == s[tail]:
                    head -= 1
                    tail += 1
                else:
                    break

            head += 1
            tail -= 1

            # if head < 0:
            #     continue
            cur_leng = tail - head + 1
            if cur_leng > len(ans):
                # print(ans, cur_leng, tail, head, s[head: tail + 1])
                ans = s[head: tail + 1]

        # even
        for i in range(n):
            head, tail = i, i + 1
            while head >= 0 and tail < n:
                if s[head] == s[tail]:
                    head -= 1
                    tail += 1
                else:
                    break

            head += 1
            tail -= 1

            # if head < 0:
            #     continue
            cur_leng = tail - head + 1
            if cur_leng > len(ans):
                ans = s[head: tail + 1]

        return ans


# ref = https://segmentfault.com/a/1190000003914228#articleHeader3
# Manacher algorithm
# N: len(s)
# TC: O(N)
# SC: O(N)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        s = "$#" + "#".join(s) + "#@"
        n = len(s)
        dp = [0] * n
        right, center = 0, 0

        for i in range(1, n - 1):
            if right > i:
                dp[i] = min(right - i, dp[2 * center - i])

            while s[i + (dp[i] + 1)] == s[i - (dp[i] + 1)]:
                dp[i] += 1

            if i + dp[i] > right:
                center, right = i, i + dp[i]

        max_radius, center_idx = max((r, i) for i, r in enumerate(dp))
        ans = s[center_idx - max_radius: center_idx + max_radius + 1].replace("#", "")
        return ans



