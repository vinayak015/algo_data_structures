"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return
            for nums in range(i, n+1):
                curr.append(nums)
                backtrack(curr, nums + 1)
                curr.pop()

        ans = []
        curr = []
        backtrack(curr, 1)

        return ans

if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n, k))