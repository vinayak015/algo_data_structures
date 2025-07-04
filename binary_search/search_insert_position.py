"""
Q35
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2

            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    key = 6
    print(sol.searchInsert(arr, key))
"""
Time Complexity: O(log(n))
"""