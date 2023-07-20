# N: len(coins)
# M: amount
#
# TC: O(NlogN + N*M), we sort coins for early break
# SC: O(N+ M), since python use Tim-Sort, it needs O(N) space
# note: table[0] = 0 is a special case

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [amount + 1] * (amount + 1)
        table[0] = 0
        coins.sort()

        for money in range(1, len(table)):
            for coin in coins:
                if coin > money:
                    break
                table[money] = min(table[money], table[money - coin] + 1)

        # print(table)

        if table[-1] < amount + 1:
            return table[-1]

        return -1


