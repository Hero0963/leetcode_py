class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        low, high = 0, m
        half_len = (m + n + 1) // 2  # a trick to find correct index

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (n + m + 1) // 2 - partition_x

            max_left_x = nums1[partition_x - 1] if partition_x != 0 else float('-inf')
            min_right_x = nums1[partition_x] if partition_x != m else float('inf')

            max_left_y = nums2[partition_y - 1] if partition_y != 0 else float('-inf')
            min_right_y = nums2[partition_y] if partition_y != n else float('inf')

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1

# learned from internet
# https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/258842/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
