# N : len(nums)
# TC: O(logN)
# SC: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head, tail = 0, len(nums) - 1
        while head <= tail:
            mid = head + (tail - head) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[tail]:
                if nums[mid] < target <= nums[tail]:
                    head = mid + 1
                else:
                    tail = mid - 1

            else:
                if nums[head] <= target < nums[mid]:
                    tail = mid - 1
                else:
                    head = mid + 1

        return -1






