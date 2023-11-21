class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [math.inf for _ in range(amount + 1)]
        table[0] = 0
        coins.sort()
        for money in range(1, len(table)):
            for coin in coins:
                if coin > money:
                    break
                table[money] = min(table[money], table[money - coin] + 1)

        if table[-1] < math.inf:
            return table[-1]

        return -1

# N: len(coins)
# M: amount
# TC: O(NlogN + N * M), we sort coins for early break
# SC: O(N + M), since python uses Tim-Sort as its built-in, it needs O(N) space