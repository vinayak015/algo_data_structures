"""
Q347
Given an integer array nums and an integer k, return the k most frequent elements. It is guaranteed that the answer is unique.
"""
from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [h[1] for h in heap]

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    k = 2
    print(sol.topKFrequent(nums, k))

"""
Time Complexity:
Counter will take O(n)
As the size of heap never increases from k, the pushing and popping will take O(log(k))
For n items pushing and popping will take O(n.log(k))
return will take O(k)
Therefore, overall time complexity becomes O(n.log(k)) 
"""

