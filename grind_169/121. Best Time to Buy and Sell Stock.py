from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = -prices[0]  # max profit after buying
        sell = 0  # max profit after selling
        for p in prices:
            buy = max(buy, -p)
            sell = max(sell, buy + p)

        return sell

# ref = https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/404998/all-in-one-o-n-time-o-1-space-python-solution/

# N: len(prices)
# TC: O(N)
# SC: O(1)
