"""
Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, ans, curr = 0, 0, 1
        if k <= 1:
            return 0

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >=k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0))
