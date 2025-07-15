"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

from typing import List
from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0 or i == 1:
                return 0
            return min(cost[i-1] + dp(i-1), cost[i-2] + dp(i-2))
        return dp(len(cost))

if __name__ == "__main__":
    cost = [10,15,20]
    # cost = [1,100,1,1,1,100,1,1,100,1]
    print(Solution().minCostClimbingStairs(cost))