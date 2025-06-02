"""
Q1167
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.
"""

from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0

        while len(sticks) > 1:
            x1 = heapq.heappop(sticks)
            x2 = heapq.heappop(sticks)
            ans += x1 + x2
            heapq.heappush(sticks, x1 + x2)
        return ans

if __name__ == "__main__":
    sol = Solution()
    sticks = [2,4,3]
    print(sol.connectSticks(sticks))

"""
Time Complexity:
Pushing and popping takes O(log(n)) and it will run for n-1 times. Hence, overall time complexity is O(n.log(n))
"""

