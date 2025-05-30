"""
Given an m x n binary (every element is 0 or 1) matrix mat, find the distance of the nearest 0 for each cell. The distance between adjacent cells (horizontally or vertically) is 1.

For example, given mat = [[0,0,0],[0,1,0],[1,1,1]], return [[0,0,0],[0,1,0],[1,2,1]].
"""

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        matrix = [row[:] for row in mat]
        m = len(matrix)
        n = len(matrix[0])
        queue = deque()
        seen = set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (next_row, next_col) not in seen and is_valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    matrix[next_row][next_col] = steps + 1
        return matrix

if __name__ == "__main__":
    sol = Solution()
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(sol.updateMatrix(mat))