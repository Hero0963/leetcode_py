# 有圖解 https://ithelp.ithome.com.tw/articles/10288610?sc=iThomeR
# N: len(nums)
# TC: O(logN)
# SC: O(N)
# note: right = mid 寫法較佳 ，因為 mid 仍有可能為答案
# 但 right = mid -1 也可，因為 ans = min(ans, nums[mid]) 有更新過

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        ans = nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            ans = min(ans, nums[mid])
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return ans
