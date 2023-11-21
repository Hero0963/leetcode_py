# N: len(words)
# K: max(len(word)) for word in words
# TC: O((N * K^2)
# SC: O(NK)


"""
Return an array of all the palindrome pairs of words.  <-- any order ??
You must write an algorithm with O(sum of words[i].length) runtime complexity. <-- maybe need trie

"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {}
        record = set()
        for i, w in enumerate(words):
            d[w[::-1]] = i

        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                prefix, postfix = w[: j], w[j:]
                if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                    record.add((i, d[prefix]))
                if postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                    record.add((d[postfix], i))


        return [list(p) for p in record]