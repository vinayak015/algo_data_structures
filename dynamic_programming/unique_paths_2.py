"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

from typing import List
from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        @cache
        def dp(row, col):
            if row < 0 or col < 0:
                return 0
            if row + col == 0:
                return 1
            if obstacleGrid[row][col] == 1:
                return 0
            ans = 0
            ans  = ans + dp(row-1, col) + dp(row, col-1)
            return ans
        return dp(m-1, n-1)


if __name__ == "__main__":
    sol = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))