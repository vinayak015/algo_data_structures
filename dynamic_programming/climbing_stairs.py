"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 1:
                return 1
            if i == 0:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        memo = {}
        ans = dp(n)
        return ans

if __name__ == "__main__":
    n = 3
    print(Solution().climbStairs(n))