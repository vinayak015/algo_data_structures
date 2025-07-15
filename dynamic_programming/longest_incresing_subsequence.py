"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""

from typing import List
from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            ans = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, dp(j) + 1)
            return ans
        ans_ = max(dp(i) for i in range(len(nums)))
        return ans_

    def lengthOfLIS_binary_search(self, nums: List[int]) -> int:
        def binary_search(arr, target):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left

        sol = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sol[-1]:
                sol.append(nums[i])
            else:
                new_idx = binary_search(sol, nums[i])
                if new_idx == len(sol):
                    continue
                sol[new_idx] = nums[i]
        return len(sol)


if __name__ == "__main__":
    nums = [1, 2, 5, 3, 4]
    nums = [10,9,2,5,3,7,101,18]
    nums =[0,1,0,3,2,3]
    nums =[7,7,7,7,7,7,7]
    nums =[1, 7, 8, 4, 5, 6, -1, 9]
    # nums =[1,3,6,7,9,4,10,5,6]
    # nums =[4,10,4,3,8,9]
    print(Solution().lengthOfLIS(nums))
    print(Solution().lengthOfLIS_binary_search(nums))