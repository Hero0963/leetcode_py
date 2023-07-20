class Solution:
    """
    n : len(s)
    time complexity: O(N), one-pass nums
    space complexity: O(N), we use cur to save visited info

    Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
    """

    def isValid(self, s: str) -> bool:
        hash_map = {")": "(", "]": "[", "}": "{"}

        cur = []
        for char in s:
            if char not in hash_map:
                cur.append(char)
            else:
                if not cur:
                    return False

                if cur.pop() != hash_map[char]:
                    return False

        if cur:
            return False

        return True
