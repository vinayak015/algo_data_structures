"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        total = 0

        for num in nums:
            total += num
            min_val = min(min_val, total)

        return -min_val + 1


if __name__ == "__main__":
    nums = [10, 20, 30]
    print(Solution().minStartValue(nums))