class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max, area = 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                diff = left_max - height[left]
                if diff > 0:
                    area += diff
                else:
                    left_max = height[left]
                left += 1
            else:
                diff = right_max - height[right]
                if diff > 0:
                    area += diff
                else:
                    right_max = height[right]
                right -= 1

        return area

# N: len(height)
# TC: O(N)
# SC: O(1)
