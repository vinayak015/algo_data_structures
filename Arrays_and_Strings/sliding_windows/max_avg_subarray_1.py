"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]
        ans = curr /k
        for right in range(k, len(nums)):
            curr += nums[right] - nums[right - k]
            ans = max(ans, curr/k)
        return ans

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(Solution().findMaxAverage(nums, k))