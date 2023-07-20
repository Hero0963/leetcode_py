# N: len(strs)
# M: max_leng of str in strs
# TC: O(M * N)
# since str[i] consists of lowercase English letters. sort counter_s TC = O(1)
# note that len(str[i]) <= 100, cost of sorting str[i] is negligible
# SC: O(N * M)


import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hash_map = collections.defaultdict(int)

        for s in strs:
            counter_s = collections.Counter(s)
            sorted_counter_s = sorted(counter_s.items(), key=lambda x: x[0])
            key_s = tuple(sorted_counter_s)
            if key_s in hash_map:
                idx = hash_map[key_s]
                ans[idx].append(s)
            else:
                hash_map[key_s] = len(ans)
                ans.append([s])

            # counter_s.clear()

        return ans


# N: len(strs)
# M: max_leng of str in strs
# TC: O(M * N)
# note that len(str[i]) <= 100, cost of sorting str[i] is negligible
# SC: O(N * M)


import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hash_map = collections.defaultdict(int)

        def helper(s):
            letters = [0] * 26
            for x in s:
                idx = ord(x) - ord('a')
                letters[idx] += 1

            # return (*letters,)
            return tuple(letters)
            # *: unpacking operator
            # equivalent to tuple(letters)

        for s in strs:
            key_s = helper(s)
            if key_s in hash_map:
                idx = hash_map[key_s]
                ans[idx].append(s)
            else:
                hash_map[key_s] = len(ans)
                ans.append([s])

            # counter_s.clear()

        return ans
