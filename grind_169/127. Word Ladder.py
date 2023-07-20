import collections


# N: len(wordList)
# M: len(beginWord)
# TC: O(N * M * 26)
# SC: O(N + N + N)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        m = len(beginWord)
        seen = collections.defaultdict(bool)
        word_set = set(wordList)
        cnt = 1

        if len(beginWord) != len(endWord):
            return 0

        if endWord not in word_set:
            return 0

        if not beginWord:
            return 0

        que = deque()
        que.append(beginWord)
        seen[beginWord] = True
        while que:
            # print("cnt = ", cnt)
            l = len(que)
            # print("que = ", que)
            for _ in range(l):
                word = que.popleft()
                if word == endWord:
                    return cnt

                for i in range(m):
                    for x in range(ord("a"), ord("z") + 1):
                        adj_word = word[:i] + chr(x) + word[i + 1:]
                        if adj_word in word_set and not seen[adj_word]:
                            que.append(adj_word)
                            seen[adj_word] = True

            cnt += 1

        return 0
