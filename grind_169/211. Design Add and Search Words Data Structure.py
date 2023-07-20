import collections


class WordDictionary:

    def __init__(self):
        self.dict_by_len = collections.defaultdict(set)

    def addWord(self, word: str) -> None:
        if word:
            self.dict_by_len[len(word)].add(word)

    def search(self, word: str) -> bool:
        if not word:
            return False

        if "." not in word:
            return word in self.dict_by_len[len(word)]

        for v in self.dict_by_len[len(word)]:
            matched = True
            for s, c in zip(word, v):
                if s != c and s != ".":
                    matched = False
                    break

            if matched:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)