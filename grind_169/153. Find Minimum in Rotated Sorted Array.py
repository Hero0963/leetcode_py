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

# N: len(nums)
# TC: O(logN)
# ref = https://ithelp.ithome.com.tw/articles/10288610
# ref = https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/698479/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/
