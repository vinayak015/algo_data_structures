"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. Return this sum. You can only move down or right.
"""

from typing import List
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if row + col == 0:
                return grid[0][0]
            ans = float("inf")
            if row > 0:
                ans = min(ans, dp(row-1, col))
            if col > 0:
                ans = min(ans, dp(row, col-1))
            return ans + grid[row][col]
        return dp(len(grid)-1, len(grid[0])-1)


if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6]]
    sol = Solution()
    print(sol.minPathSum(grid))