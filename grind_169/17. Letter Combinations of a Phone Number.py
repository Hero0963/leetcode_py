import collections


# N: len(digits)
# TC: O(N)
# SC: O(N)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.ans = [""]
        hash_map = collections.defaultdict(list)
        hash_map["2"] = ["a", "b", "c"]
        hash_map["3"] = ["d", "e", "f"]
        hash_map["4"] = ["g", "h", "i"]
        hash_map["5"] = ["j", "k", "l"]
        hash_map["6"] = ["m", "n", "o"]
        hash_map["7"] = ["p", "q", "r", "s"]
        hash_map["8"] = ["t", "u", "v"]
        hash_map["9"] = ["w", "x", "y", "z"]

        n = len(digits)

        def helper(letters):
            if len(self.ans[0]) == n:
                return

            new_ans = []
            for letter in letters:
                for s in self.ans:
                    new_ans.append(s + letter)

            self.ans = new_ans

        for num in digits:
            letters = hash_map[num]
            helper(letters)

        return self.ans


import collections


# N: len(digits)
# TC: O(N)
# SC: O(N)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.ans = [""]
        hash_map = collections.defaultdict(list)
        hash_map["2"] = ["a", "b", "c"]
        hash_map["3"] = ["d", "e", "f"]
        hash_map["4"] = ["g", "h", "i"]
        hash_map["5"] = ["j", "k", "l"]
        hash_map["6"] = ["m", "n", "o"]
        hash_map["7"] = ["p", "q", "r", "s"]
        hash_map["8"] = ["t", "u", "v"]
        hash_map["9"] = ["w", "x", "y", "z"]

        n = len(digits)

        def helper(i):
            if i == n:
                return

            new_ans = []
            num = digits[i]
            letters = hash_map[num]
            for letter in letters:
                for s in self.ans:
                    new_ans.append(s + letter)

            self.ans = new_ans
            helper(i + 1)

        helper(0)
        return self.ans
