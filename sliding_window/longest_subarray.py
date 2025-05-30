"""
Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.
"""
from typing import List

def longest_subarray(nums: List, k: int ):
    left = curr_sum = ans = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans