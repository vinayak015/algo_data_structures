"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagnols, anti_diagnols, cols):
            if row == n:
                return 1

            sol = 0
            for col in range(n):
                curr_diag = row - col
                curr_anti_diag = row + col
                if (col in cols or curr_diag in diagnols or curr_anti_diag in anti_diagnols):
                    continue
                cols.add(col)
                diagnols.add(curr_diag)
                anti_diagnols.add(curr_anti_diag)

                sol += backtrack(row + 1, diagnols, anti_diagnols, cols)

                cols.remove(col)
                diagnols.remove(curr_diag)
                anti_diagnols.remove(curr_anti_diag)

            return sol

        ans = backtrack(0, set(), set(), set())
        return ans




if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.totalNQueens(n))
