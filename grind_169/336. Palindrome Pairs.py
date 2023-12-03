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

# N: len(words)
# K: max(len(word)) for word in words
# TC: O((NK)^2)
# SC: O(NK)
# can be optimized by Manacher's algorithm
