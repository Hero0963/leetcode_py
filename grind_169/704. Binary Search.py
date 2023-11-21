class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head, tail = 0, len(nums) - 1
        while head <= tail:
            mid = head + (tail - head) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid - 1
            else:
                head = mid + 1

        return -1


# N: len(nums)
# TC: O(logN)
# SC: O(1)