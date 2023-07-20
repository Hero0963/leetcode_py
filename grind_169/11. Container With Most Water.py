# N: len(height)
# TC: O(N)
# SC: O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        head, tail = 0, len(height) - 1
        ans = 0
        while head < tail:
            l_height, r_height = height[head], height[tail]
            h = min(l_height, r_height)
            w = tail - head
            cur_area = h * w
            ans = max(ans, cur_area)

            if l_height < r_height:
                head += 1
            else:
                tail -= 1

        return ans
