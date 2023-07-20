class Solution:
    """
    N : len(s)
    time complexity: O(N)
    space complexity: O(1)

    Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.

    we can also use some built-in functions, or regex

    """

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


def is_alphabet_num(s: str) -> bool:
    if ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9'):
        return True


def convert_to_lowercase(s: str) -> str:
    if ord('A') <= ord(s) <= ord('Z'):
        return chr(ord(s) - ord('A') + ord('a'))
    else:
        return s
