"""
Given an array of positive integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits).
Return -1 if there is no pair of numbers with the same digit sum.
"""

from collections import defaultdict
from typing import List


class Solution:
    def max_sum(self, nums: List[int]) -> int:

        def digit_sum(num):
            sum_ = 0
            while num:
                sum_ += num % 10
                num //= 10
            return sum_

        hashmap = defaultdict(int)

        max_ = -1
        for idx, num in enumerate(nums):
            sum_ = digit_sum(num)
            if sum_ in hashmap:
                max_ = max(max_, num + hashmap[sum_])

            hashmap[sum_] = max(num, hashmap[sum_])
        return max_


if __name__ == "__main__":
    nums = [18,43,36,13,7, 54]
    print(Solution().max_sum(nums))
