"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').

You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze.

Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
"""

from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] != "+"

        def is_border(row, col):
            return row == m-1 or row == 0 or col == n-1 or col == 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(maze)
        n = len(maze[0])
        seen = {(*entrance, )}
        queue = deque([(*entrance, 0)])

        while queue:
            row, col, steps = queue.popleft()
            if is_border(row, col) and (row, col) != (entrance[0], entrance[1]):
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if is_valid(next_row, next_col):
                    if (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col, steps + 1))
        return -1

if __name__ == "__main__":
    sol = Solution()
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    print(sol.nearestExit(maze, entrance))