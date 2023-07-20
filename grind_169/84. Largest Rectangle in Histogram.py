# ref = https://www.cnblogs.com/boring09/p/4231906.html
# ref = https://fuxuemingzhu.cn/leetcode/84.html

# N: len(heights)
# TC: O(N)
# SC: O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        heights.append(0)
        area = 0

        for x, y in enumerate(heights):
            if not stack or y > heights[stack[-1]]:
                stack.append(x)
            else:
                while stack and y <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = x if not stack else x - stack[-1] - 1
                    area = max(area, h * w)
                stack.append(x)

        return area
