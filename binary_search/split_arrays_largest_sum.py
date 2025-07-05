"""
Q410
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
"""

from typing import List

class Solution:
    def splitArray_(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2

            curr_sum = 0
            sub_array = 1
            for num in nums:
                if curr_sum + num <= mid:
                    curr_sum += num
                else:
                    sub_array += 1
                    curr_sum = num
            if sub_array <= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [7,2,5,10,8]
    k = 2
    print(sol.splitArray_(nums, k))

"""
Time complexity:
    n = len(nums)
    m = left - right
    Overall complexity: O(n.log(m))
"""
