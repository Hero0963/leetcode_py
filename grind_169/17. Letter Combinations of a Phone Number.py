import collections


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = collections.defaultdict(str)
        digit_to_letters["2"] = "abc"
        digit_to_letters["3"] = "def"
        digit_to_letters["4"] = "ghi"
        digit_to_letters["5"] = "jkl"
        digit_to_letters["6"] = "mno"
        digit_to_letters["7"] = "pqrs"
        digit_to_letters["8"] = "tuv"
        digit_to_letters["9"] = "wxyz"

        n = len(digits)
        self.ans = []
        self.comb = []

        def backtrack(i):
            if i == n:
                self.ans.append("".join(self.comb))
                return

            num = digits[i]
            letters = digit_to_letters[num]
            for letter in letters:
                self.comb.append(letter)
                backtrack(i + 1)
                self.comb.pop()

        backtrack(0)
        return self.ans

# N: # of d in "234568" as input
# M: # of d in "79" as input
# Let L = N + M
# TC: O(3^N*4^M) <= O(4^L)
# SC: O(N + M) = O(L)
