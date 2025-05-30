"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
"""

from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        frequency_hash = {}
        nums.sort()
        for num in nums:
            frequency_hash[num] = frequency_hash.get(num, 0) + 1

        for num in nums[::-1]:
            count = frequency_hash.get(num, 0)
            if count == 1:
                return num
        return -1

    def largestUniqueNumber_(self, nums: List[int]) -> int:
        frequency_hash = {}
        for num in nums:
            frequency_hash[num] = frequency_hash.get(num, 0) + 1
        max_ = -1
        for num in nums:
            count = frequency_hash.get(num, 0)
            if count == 1:
                max_ = max(max_, num)
        return max_


if __name__ == "__main__":
    sol = Solution()
    nums = [5,7,3,9,4,9,8,3,1]
    print(sol.largestUniqueNumber(nums=nums))




