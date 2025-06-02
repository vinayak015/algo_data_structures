"""
Q1962
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove ceil(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

ceil(x) is the smallest integer that is greater than or equal to x (i.e., rounds x up).
"""

from typing import List
import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-stone for stone in piles]
        heapq.heapify(heap)

        for i in range(k):
            x = -heapq.heappop(heap)
            x = math.ceil(x/2)
            heapq.heappush(heap, -x)

        return -sum(heap)

if __name__ == "__main__":
    sol = Solution()
    piles = [4,3,6,7]
    k = 3
    print(sol.minStoneSum(piles, k))

"""
Time Complexity:
Creating heaps O(n)

"""
