class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        head, tail = 0, n - 1
        pos = n - 1
        while pos >= 0:
            h_square = nums[head] ** 2
            t_square = nums[tail] ** 2
            if h_square >= t_square:
                ans[pos] = h_square
                head += 1
            else:
                ans[pos] = t_square
                tail -= 1

            pos -= 1

        return ans

# N: len(nums)
# TC: O(N)
# SC: O(N)
