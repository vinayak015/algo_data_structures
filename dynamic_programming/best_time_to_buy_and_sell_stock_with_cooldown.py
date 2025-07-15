"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, is_holding, is_cooldown):
            if i == len(prices):
                return 0
            if is_holding:
                skip = dp(i + 1, is_holding, is_cooldown)
                sell = prices[i] + dp(i+1, not is_holding, True)
                return max(skip, sell)
            elif not is_holding and is_cooldown:
                skip = dp(i + 1, is_holding, False)
                return skip
            else:
                skip = dp(i + 1, is_holding, is_cooldown)
                buy = -prices[i] + dp(i+1, not is_holding, False)
                return max(buy, skip)
        return dp(0, False, False)


if __name__ == "__main__":
    sol = Solution()
    prices = [1, 2, 3, 0, 2]
    print(sol.maxProfit(prices))