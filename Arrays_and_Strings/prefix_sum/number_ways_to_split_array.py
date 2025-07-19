"""
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

"""
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])

        ans = 0
        n = len(nums)
        for i in range(n-1):
            left_sum = prefix[i]
            right_sum = prefix[n-1] - prefix[i]
            if left_sum > right_sum:
                ans += 1
        return ans

if __name__ == "__main__":
    nums = [2,3,1,0]
    print(Solution().waysToSplitArray(nums))
