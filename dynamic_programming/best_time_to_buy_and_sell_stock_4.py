"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

from typing import List
from functools import cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i, holding, remain):
            if i == len(prices) or remain == 0:
                return 0
            skip = dp(i + 1, holding, remain)

            if holding:
                sell = prices[i] + dp(i+1, not holding, remain-1)
                return max(sell, skip)
            else:
                buy = -prices[i] + dp(i+1, not holding, remain)
                return max(buy, skip)
        ans = dp(0, False, k)
        return ans
if __name__ == "__main__":
    k = 2
    # prices = [2,4,1]
    prices = [3,2,6,5,0,3]
    sol = Solution()
    print(sol.maxProfit(k, prices))