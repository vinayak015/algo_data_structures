"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}
        count = 0
        max_len = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in count_map:
                max_len = max(max_len, i - count_map[count])
            else:
                count_map[count] = i
        return max_len



if __name__ == "__main__":
    sol = Solution()
    nums = [0,1, 0, 0, 0, 1, 1, 0]
    print(sol.findMaxLength(nums))


