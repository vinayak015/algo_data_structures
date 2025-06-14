"""
Q502
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources,
it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.
"""

from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        n = len(projects)
        i = 0
        heap = []
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if len(heap) == 0:
                # not enough money to do any more projects
                return w
            w -= heapq.heappop(heap)
        return w


if __name__ == "__main__":
    sol = Solution()
    profits = [3, 1, 6, 12, 20]
    capital = [0, 0, 2, 5, 7]
    k = 3
    w = 1
    print(sol.findMaximizedCapital(k, w, profits, capital))

"""
Time Complexity:
We do (k + n) times push and pop operation in the heap. Each operation takes log(n), where n is the length of capital. 
Therefore total time complexity becomes ((k + n).log(n))

Space Complexity: O(n) because of the heap creation
"""

