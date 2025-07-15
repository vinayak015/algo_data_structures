"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner and wants to move to the bottom-right corner.

The robot can only move either down or right. Given m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""
from linecache import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(row, col):
            if row + col == 0:
                return 1
            ways = 0
            if row > 0:
                ways += dp(row-1, col)
            if col > 0:
                ways += dp(row, col-1)
            return ways
        return dp(m-1, n-1)

if __name__ == "__main__":
    m = 3
    n = 2
    sol = Solution()
    print(sol.uniquePaths(m, n))
