"""
Q909
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.
"""

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        columns = list(range(n))
        label = 1
        for row in range(n-1, -1, -1):
            for col in columns:
                cells[label] = (row, col)
                label += 1
            columns.reverse()

        dist = [-1] * (n**2+1)
        queue = deque([1])
        dist[1] = 0

        while queue:
            curr = queue.popleft()
            for next_ in range(curr + 1, min(curr + 6, n ** 2) + 1):
                n_row, n_col = cells[next_]
                destination = board[n_row][n_col] if board[n_row][n_col] != -1 else next_

                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    queue.append(destination)
        return dist[-1]

if __name__ == "__main__":
    sol = Solution()
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    print(sol.snakesAndLadders(board))
