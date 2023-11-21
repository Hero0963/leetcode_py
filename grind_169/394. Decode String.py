class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string, cur_num = "", 0

        for c in s:
            if c == "[":
                stack.append(((cur_string, cur_num)))
                cur_string, cur_num = "", 0

            elif c == "]":
                pre_string, repeat_times = stack.pop()
                cur_string = pre_string + cur_string * repeat_times

            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)

            else:
                cur_string += c

        return cur_string

# N: len(s)
# L: real length after decoding, L < 10^N
# TC: O(L), need to decode each substring
# SC: O(L)
