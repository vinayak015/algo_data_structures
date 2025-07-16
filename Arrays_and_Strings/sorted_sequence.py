"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Without using sort
"""

from typing import List

class Solution:
    # Note: We can dp this because nums is already a sorted array
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left, right = 0, len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            ans[i] = square * square
        return ans

if __name__ == "__main__":
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
