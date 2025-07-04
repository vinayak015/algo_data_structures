"""
Q12813
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor,
divide all the array by it, and sum the division's result.
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
"""

from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(div):
            _sum = 0
            for num in nums:
                _sum += math.ceil(num / div)
            return _sum <= threshold

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()
    nums = [44,22,33,11,1]
    threshold = 5
    print(sol.smallestDivisor(nums, threshold))

"""
Time Complexity:
    n = len(nums)
    k = max(nums)
    Overall Complexity: O(n.log(k))
"""
