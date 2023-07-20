# ref = https://leetcode.com/problems/decode-string/solutions/941345/python-o-n-by-stack-w-comment/


# N: len(s)
# L: real length after decoded, L < 10^N
# TC: O(L), need to decode each substring
# SC: O(L)
# similar to basic calculator

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_token, cur_number = "", 0

        for char in s:
            if char == "[":
                stack.append((cur_token, cur_number))
                cur_token, cur_number = "", 0

            elif char == "]":
                prev_token, repeat_times = stack.pop()
                cur_token = prev_token + repeat_times * cur_token

            elif char.isdigit():
                cur_number = cur_number * 10 + int(char)

            else:
                cur_token += char

        return cur_token
