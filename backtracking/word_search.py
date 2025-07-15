"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def backtrack(row, col, i, seen):
            if i == len(word):
                return True

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                    if board[next_row][next_col] == word[i]:
                        seen.add((next_row, next_col))
                        if backtrack(next_row, next_col, i+1, seen):
                            return True
                        seen.remove((next_row, next_col))
            return False

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    print(sol.exist(board, word))