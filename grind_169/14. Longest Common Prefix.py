# ref = https://leetcode.com/problems/longest-common-prefix/solutions/6918/short-python-solution/

# N: len(strs)
# M: len(shortest_str)
# TC: O(N + N*M)
# SC: O(M), as return

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            for s in strs:
                if s[i] != char:
                    return shortest_str[:i]

        return shortest_str


# ref = https://fuxuemingzhu.cn/leetcode/14.html#%E6%8E%92%E5%BA%8F


# N: len(strs)
# M: max_leng element in strs
# TC: O(MNlogN + M)
# SC: O(NM) for sort

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        size = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < size and strs[0][i] == strs[-1][i]:
            i += 1

        return strs[0][:i]