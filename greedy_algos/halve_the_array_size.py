"""
Q1338
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

"""

from typing import List
from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        counts = [count for number, count in counts.most_common()]
        removed = 0
        ans = 0
        half = len(arr) // 2
        for count in counts:
            removed += count
            ans += 1
            if removed > half:
                break
        return ans



if __name__ == "__main__":
    sol = Solution()
    arr = [3, 5, 4, 3, 2, 6, 2, 2, 1, 9, 7, 5]
    # arr = [1,1,1,1,1, 2,3,4,5, 6]
    # arr = [3,3,3,3,5,5,5,2,2,7]
    print(sol.minSetSize(arr))


"""
Time Complexity:
    n: len(arr)
    Counter takes: O(n)
    Extracting most common ones: O(n.log(n))
    
    Overall Complexity: O(n.log(n))

"""