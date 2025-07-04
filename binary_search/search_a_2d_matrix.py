"""
Q74
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        left, right = 0, (r * c) -1

        while left <= right:
            mid = (left + right) // 2
            row = mid // c
            col = mid % c

            if matrix[row][col] == target:
                return True
            if target < matrix[row][col]:
                right = mid - 1
            else:
                left = mid + 1
        return False

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(sol.searchMatrix(matrix, target))

"""
Time Complexity: O(log(m.n))
"""