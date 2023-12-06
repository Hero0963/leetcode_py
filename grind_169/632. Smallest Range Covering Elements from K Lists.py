import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        range_left, range_right = -math.inf, math.inf
        max_value = max(vec[0] for vec in nums)
        priority_queue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priority_queue)

        while True:
            min_value, row, idx = heapq.heappop(priority_queue)
            if max_value - min_value < range_right - range_left:
                range_left, range_right = min_value, max_value
            if idx == len(nums[row]) - 1:
                break
            max_value = max(max_value, nums[row][idx + 1])
            heapq.heappush(priority_queue, (nums[row][idx + 1], row, idx + 1))

        return [range_left, range_right]


# ref = https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/solutions/355881/zui-xiao-qu-jian-by-leetcode-solution/
# 该问题可以转化为，从 k 个列表中各取一个数，使得这 k 个数中的最大值与最小值的差最小。


from sortedcontainers import SortedList
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        range_left, range_right = -math.inf, math.inf
        max_value = max(vec[0] for vec in nums)

        sorted_list = SortedList([(-vec[0], i, 0) for i, vec in enumerate(nums)])

        while True:
            _value, row, idx = sorted_list.pop()
            min_value = -_value
            if max_value - min_value < range_right - range_left:
                range_left, range_right = min_value, max_value
            if idx == len(nums[row]) - 1:
                break
            max_value = max(max_value, nums[row][idx + 1])
            sorted_list.add((-nums[row][idx + 1], row, idx + 1))

        return [range_left, range_right]
