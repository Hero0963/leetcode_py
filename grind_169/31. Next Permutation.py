# N: len(nums)
# TC: O(N)
# SC: O(1)
# note:
# nums.verse() costs O(1) SC
# C++ supports next_permutation function

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        flip_idx, filp_val = 0, math.inf
        j = n - 1
        while j > 0:
            if nums[j - 1] < nums[j]:
                flip_idx = j - 1
                filp_val = nums[flip_idx]
                break
            else:
                j -= 1

        # next_permutation is the lowest order
        if filp_val == math.inf:
            nums.reverse()
            return

        cur_min_val = math.inf
        cur_min_idx = flip_idx
        for i in range(flip_idx + 1, n):
            # = is important, since we will reverse the array later
            if filp_val < nums[i] <= cur_min_val:
                cur_min_val = nums[i]
                cur_min_idx = i

        nums[flip_idx], nums[cur_min_idx] = nums[cur_min_idx], nums[flip_idx]
        # swapping values makes more sense to the below
        # filp_val, cur_min_val = cur_min_val, filp_val

        head, tail = flip_idx + 1, n - 1
        while head < tail:
            nums[head], nums[tail] = nums[tail], nums[head]
            head += 1
            tail -= 1
