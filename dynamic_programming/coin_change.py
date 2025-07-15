"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List
from functools import cache, lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @lru_cache(None)
        @cache
        def dp(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_result = float("inf")
            for coin in coins:
                res = dp(rem - coin)
                if res != -1:
                    min_result = min(min_result, res + 1)
            return min_result if min_result != float("inf") else -1

        return dp(amount)

if __name__ == "__main__":
    coins = [186,419,83,408]
    coins = [1,2,5]
    amount = 6249
    amount = 13
    print(Solution().coinChange(coins, amount))

