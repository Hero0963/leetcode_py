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


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True


class WordDictionary:
    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(index + 1, child):
                    return True
            else:
                for child in node.children:
                    if child is not None and dfs(index + 1, child):
                        return True
            return False

        return dfs(0, self.trieRoot)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/design-add-and-search-words-data-structure/solution/tian-jia-yu-sou-suo-dan-ci-shu-ju-jie-go-n4ud/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# note:
# add: 可用 length 當 key, 保存到 set 中
# search 時，看是否存在
# N: total words
# L: max_length of words
# TC: O(L * N)
# SC: O(N * L)
#
#
# trie:
# add: wood -> woods，會往下造 26 個字 wooda, woodb,... 並標註 woods.isEnd = True
# search: 逐字匹配
# N: total words
# L: max_length of words
# TC: O(L)
# SC: O(26^L)
