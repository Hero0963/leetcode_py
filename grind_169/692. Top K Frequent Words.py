import collections


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

# N: len(words), N <= 500
# L: max_length of element in words, L <= 10, so we may consider L as a const
# M: max_count in groups, M <= N
# G: the number of group to reverse visiting greoup to obtain k elements, G <= len(groups)
# TC: O(N + N + G * MlogM), where the last term is to estimate sorting cost
# SC: O(N + N + N)
