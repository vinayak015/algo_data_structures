"""
Q1481
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
"""

from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        freq = sorted(count.values(), reverse=True)
        while k:
            if freq[-1] <= k:
                k -= freq[-1]
                freq.pop()
            else:
                break
        return len(freq)

if __name__ == "__main__":
    arr = [4,3,1,1,3,3,2]
    k = 3
    sol = Solution()
    print(sol.findLeastNumOfUniqueInts(arr, k))

"""
Time Complexity:
sorting: O(n.log(n))
while loop: O(k)
Since, k > n, therefore O(n.log(n))

Space complexity: O(n) due to hashmap and freq
"""