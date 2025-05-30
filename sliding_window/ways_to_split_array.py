"""
Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section.
The second section should have at least one number.
"""

from typing import List

def ways_to_split_array(nums: List):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0

    for i in range(0, len(nums)-1):
        left = prefix[i]
        right = prefix[-1] - prefix[i]

        if left >= right:
            ans += 1
    return ans

print(ways_to_split_array([10, 4, -8, 7]))


def another_way_to_split_array(nums: List):
    total = sum(nums)
    left = 0
    ans = 0
    for i in range(len(nums)-1):
        left += nums[i]
        right = total - left
        if left >= right:
            ans += 1

    return ans

print(another_way_to_split_array([10, 4, -8, 7]))
