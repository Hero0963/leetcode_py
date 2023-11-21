class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# Define dp[i] = length of LIS in [0, i]
# N: len(nums)
# TC: O(N^2)
# SC: O(N)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []

        for num in nums:
            insertion_pos = bisect_left(arr, num)

            if insertion_pos == len(arr):
                arr.append(num)
            else:
                arr[insertion_pos] = num

        return len(arr)


# N: len(nums)
# TC: O(NlogN)
# SC: O(N)

# ref = https://leetcode.com/problems/longest-increasing-subsequence/solutions/1484417/Python-O(NlogN)/
"""
example: [1, 2, 4, 5, 3, 11]
insert 1 --> 1
insert 2 --> 1, 2
insert 4 --> 1, 2, 4
insert 5 --> 1, 2, 4, 5
insert 3 --> 1, 2, 3, 5
insert 11 -->1, 2, 3, 5, 11  (note that this is not the LIS)
"""
# to find really LIS: https://zh.wikipedia.org/wiki/%E6%9C%80%E9%95%BF%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97

#: other variations: https://web.ntnu.edu.tw/~algo/Subsequence.html