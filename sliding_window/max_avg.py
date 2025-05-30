from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sum_ = 0
        for i in range(k):
            sum_ += nums[i]
        ans = sum_ / k
        for i in range(k, len(nums)):
            sum_ += nums[i] - nums[i - k]
            avg = sum_ / k
            ans = max(ans, avg)
        return ans

s = Solution()
print(s.findMaxAverage([5, 2, 3,4], 2))