"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
"""

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        n = len(nums)
        ans = [-1] * n
        for i in range(k, n - k):
            ans[i] = (prefix[i + k] - prefix[i - k] + nums[i-k]) // (2*k + 1)
        return ans

if __name__ == "__main__":
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    print(Solution().getAverages(nums, k))