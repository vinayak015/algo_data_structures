"""
Q215
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(sol.findKthLargest(nums, k))

"""
Time Complexity:
creating heap will take O(n)
pushing and popping k-1 elements will take O(k.log(n)), in the worst case k=n.
Overall Time Complexity: O(n.log(n))
"""
