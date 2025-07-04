"""
Q1196
You have some apples and a basket that can carry up to 5000 units of weight.

Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you can put in the basket.
"""

from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans = 0
        max_w = 5000
        total_w = 0
        for w in weight:
            total_w += w
            if total_w <= max_w:
                ans += 1
            else:
                break
        return ans

if __name__ == "__main__":
    sol = Solution()
    weight = [1000,1000,1000,1000,1000]
    print(sol.maxNumberOfApples(weight))
