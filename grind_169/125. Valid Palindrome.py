def is_alphabet_num(s: str) -> bool:
    return ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9')


def convert_to_lowercase(s: str) -> str:
    if ord('A') <= ord(s) <= ord('Z'):
        return chr(ord(s) - ord('A') + ord('a'))
    return s


class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1

        while head <= tail:
            if not is_alphabet_num(s[head]):
                head += 1
                continue
            if not is_alphabet_num(s[tail]):
                tail -= 1
                continue

            ch = convert_to_lowercase(s[head])
            ct = convert_to_lowercase(s[tail])

            if ch != ct:
                return False

            head += 1
            tail -= 1

        return True


# N: len(s)
# TC: O(N)
# sC: O(1)
