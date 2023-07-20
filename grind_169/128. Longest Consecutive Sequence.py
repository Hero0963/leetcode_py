import collections


# N: len(nums)
# TC: O(N)
# SC: O(N), which can be reduced by using hash_map = defaultdict(bool) only

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 1
        counter = collections.Counter(nums)
        visited = collections.defaultdict(bool)

        for num in counter.keys():
            visited[num] = True
            i, j = num - 1, num + 1

            while True:
                if visited[i] or i not in counter:
                    break

                visited[i] = True
                i -= 1

            while True:
                if visited[j] or j not in counter:
                    break

                visited[j] = True
                j += 1

            cnt = j - i - 1
            # print("num, i, j = ", num, i, j)
            if cnt > ans:
                ans = cnt

        # print("visited = ", visited)

        return ans
