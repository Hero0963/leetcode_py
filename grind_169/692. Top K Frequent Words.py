import collections


# N: len(words)
# M: max val of the same count, it may influence sort efficient
# TC: O(N + N + KlogM)
# SC: O(N + N + N)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        groups = collections.defaultdict(list)

        max_val, min_val = -1, len(words) + 1
        for key, val in counter.items():
            groups[val].append(key)
            max_val = max(max_val, val)
            min_val = min(min_val, val)

        ans = []
        for v in range(max_val, min_val - 1, -1):
            words_list = groups[v]
            words_list.sort()
            for x in words_list:
                if len(ans) == k:
                    break
                ans.append(x)

        return ans


from typing import List
from collections import Counter


class Solution:
    """
    N: len(words)
    M: number of elements in words, M<=N
    K: k
    time complexity: O(N+MlogM+K)
    space complexity: O(M+K)

    Constraints:

    1 <= words.length <= 500
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    k is in the range [1, The number of unique words[i]]

    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        sorted_c = sorted(c.items(), key=lambda vals: (-vals[1], vals[0]))

        ans = []

        for i in range(k):
            if i < len(sorted_c):
                ans.append(sorted_c[i][0])


from typing import List
from collections import Counter
from heapq import nsmallest


# ref= https://blog.51cto.com/u_15302258/3076064 , using heap
# ref= https://ithelp.ithome.com.tw/articles/10247299
# ref= https://leetcode.com/problems/top-k-frequent-words/discuss/573662/Python-2-lines-heap

class Solution:
    """
    time complexity: O(NlogK)
    space complexity: O(N)
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)

        # to avoid len(c)
        goal = min(k, len(c))

        ans = nsmallest(goal, c.keys(), key=lambda x: (-c[x], x))

        return ans