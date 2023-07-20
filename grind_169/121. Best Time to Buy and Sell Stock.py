# ref = https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/404998/all-in-one-o-n-time-o-1-space-python-solution/

from typing import List


class Solution:
    """
    N: len(prices)
    time complexity: O(N), one-pass
    space complexity: O(1)

    Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4

    """

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        cost = prices[0]
        profit = 0

        for p in prices:
            cost = min(cost, p)
            profit = max(profit, p - cost)

        return profit
