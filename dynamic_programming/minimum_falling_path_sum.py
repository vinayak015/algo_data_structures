"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""
from typing import List
from functools import cache


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def dp(row, col):
            if row < 0 or col < 0 or col > n-1:
                return float("inf")
            if row == 0:
                return matrix[row][col]
            ans = float("inf")
            ans = min(ans, dp(row-1, col), dp(row-1, col-1), dp(row-1, col+1)) + matrix[row][col]
            return ans
        return min(dp(m-1, col) for col in range(n))


if __name__ == "__main__":
    sol = Solution()
    matrix = [[-19,57],[-40,-5]]
    print(sol.minFallingPathSum(matrix))