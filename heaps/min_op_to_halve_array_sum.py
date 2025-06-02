"""
Q2208
You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)

Return the minimum number of operations to reduce the sum of nums by at least half.
"""

from typing import List
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)

        moves = 0
        while target > 0:
            moves += 1
            x = heapq.heappop(heap)
            half = x / 2
            target += half
            heapq.heappush(heap, half)

        return moves

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 8, 20]
    print(sol.halveArray(nums))

"""
Time Complexity:
target, heap, heapify = O(n), O(n), O(n)
while loop: 
    heappop, heappush = O(log(n)), O(log(n))
In the worst case loop has to iterate n times, therefore, the time complexity is O(n.log(n)) 
"""


