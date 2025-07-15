"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
"""

from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, holding):
            if i == len(prices):
                return 0
            skip = dp(i + 1, holding)
            if holding:
                sell = prices[i] + dp(i + 1, not holding) - fee

                return max(sell, skip)
            else:
                buy = -prices[i] + dp(i + 1, not holding)
                # skip = dp(i+1, holding)
                return max(buy, skip)

        return dp(0, False)

if __name__ == "__main__":
    prices = [1,3,7,5,10,3]
    fee = 3
    sol = Solution()
    print(sol.maxProfit(prices, fee))