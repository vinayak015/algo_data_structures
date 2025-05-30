
from typing import List
class Solution_:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        min_ = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i] + prefix[-1]
            prefix.append(curr)
            if curr < min_:
                min_ = curr
        if min_ <= 0:
            return abs(min_) + 1
        if min_ >= 1:
            return 1



class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mini = 0
        prefix = [nums[0]]
        mini = min(prefix[0], mini)
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
            mini = min(mini, prefix[-1])
        return 1 - mini

s = Solution()
print(s.minStartValue([1, 2]))