"""
Q1631
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""

from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row <m and 0 <= col < n

        def check(effort):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            seen = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                row, col = stack.pop()
                if (row, col) == (m-1, n-1):
                    return True
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
            return False


        m, n = len(heights), len(heights[0])
        left = 0
        right = max(max(row for row in heights))

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    sol = Solution()
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    print(sol.minimumEffortPath(heights))

"""
Time Complexity:
    m, n = len(heights), len(heights[0])
    k = max(heights)
    DFS: O(m.n)
    binary_search: O(log(k))
    
    Overall Complexity: O(m.n.log(k))
"""