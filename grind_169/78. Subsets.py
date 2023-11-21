class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subset = []
        bag = []

        # ----------------------------------------
        def picker(i: int):
            ## Base case aka stop condition
            # Terminate when all items are taken into consideration

            if i == len(nums):
                all_subset.append(bag[::])
                return

            ## General cases:

            # Option_1: pick current item on index i
            bag.append(nums[i])
            picker(i + 1)
            bag.pop()

            # Option_2: not to pick current item on index i
            picker(i + 1)

            return
            # -----------------------------------------

        # Let's start item picking from index 0
        picker(0)

        # 返回最終結果(所有可能的情況)
        return all_subset


# ref = # ref = https://medium.com/@cutesciuridae/%E8%A9%B3%E8%A7%A3-subset-%E5%95%8F%E9%A1%8C-%E6%90%AD%E9%85%8Dleetcode%E5%B9%B3%E5%8F%B0-56d1817508a1
# N: len(nums)
# TC: O(N ^ 2 * N)
# SC: O(N ^ 2 * N)
# note: Bit Manipulation can reduce SC


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all_subsets = []

        for i in range(2 ** n):
            subset = []
            for j in range(n):
                # 檢查二進制表示中的每一位是否為1，如果是，則將對應的元素添加到子集中
                if (i >> j) & 1:
                    subset.append(nums[j])
            all_subsets.append(subset)

        return all_subsets

# by chatgpt
