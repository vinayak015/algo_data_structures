"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

from collections import defaultdict
from typing import List

class Solution:
    def equal_pairs(self, grid: List[List[int]]) -> int:
        row_map = defaultdict(int)
        col_map = defaultdict(int)

        def convert_to_tuple(arr):
            return tuple(arr)

        for row in grid:
            row_map[convert_to_tuple(row)] += 1
        for col in range(len(grid[0])):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])
            col_map[convert_to_tuple(column)] += 1

        ans = 0
        for row in row_map:
            ans += col_map[row] * row_map[row]
        return ans




if __name__ == "__main__":
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(Solution().equal_pairs(grid))
