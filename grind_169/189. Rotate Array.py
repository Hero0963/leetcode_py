# N: len(nums)
# TC: O(N)
# SC: O(1)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        if k == 0:
            return

        def reverse_array(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse_array(nums, 0, n - 1)
        reverse_array(nums, 0, k - 1)
        reverse_array(nums, k, n - 1)


"""
   WLOG, k = k % n
   consider [a0, a1, a2, ... a_k-1, a_k, ... a_n-1]
   goal = [ak, a_k+1, ... a_n-1  | a0, a1, a2, ... a_k-1]

   step1 -> [a_n-1, a_n-2, ... a_k | a_k-1, ... a1, a0]
   step2 -> [a_k, a_k+1, ...  a_n-1| a_k-1, ... a1, a0]
   step3 -> [a_k, a_k+1, ...  a_n-1| a0, a1, a2, ... a_k-1]
   done
"""
