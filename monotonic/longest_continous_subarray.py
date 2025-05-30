"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
"""

from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left, ans = 0, 0

        for right in range(len(nums)):
            while increasing and increasing[-1] < nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] > nums[right]:
                decreasing.pop()

            increasing.append(nums[right])
            decreasing.append(nums[right])

            while increasing[0] - decreasing[0] > limit:
                if increasing[0] == nums[left]:
                    increasing.popleft()
                if decreasing[0] == nums[left]:
                    decreasing.popleft()
                left += 1
            ans = max(ans, right - left + 1)

        return  ans


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 1, 2, 4, 7, 2]
    # nums = [4,2,2,2,4,4,2,2]
    limit = 5
    # limit = 0
    print(sol.longestSubarray(nums, limit))
