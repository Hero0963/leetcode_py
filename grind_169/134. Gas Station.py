# N: len(gas)
# TC: O(N)
# SC: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, end, move = 0, 0, 0
        remaining_gas = gas[start] - cost[start]

        while move < n:
            if remaining_gas >= 0:
                end = (end + 1) % n
                remaining_gas += gas[end] - cost[end]
            else:
                start = (start - 1) % n
                remaining_gas += gas[start] - cost[start]

            move += 1

        if remaining_gas >= 0:
            return start

        return -1
