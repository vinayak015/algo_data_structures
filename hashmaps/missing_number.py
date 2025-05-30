"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Space complexity: O(1), time complexity O(2n)= O(n)
        :param nums:
        :return:
        """
        nums.sort()
        for i in range(0, len(nums)+1):
            if i < len(nums) and i - nums[i] == 0 :
                continue
            else:
                return i
    def missingNumber2(self, nums: List[int]) -> int:
        """
        Space complexity: O(n), time complexity O(2n)= O(n)
        :param nums:
        :return:
        """
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
