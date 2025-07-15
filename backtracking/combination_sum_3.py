"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(idx, curr):
            if len(path) == k and curr == n:
                ans.append(path[:])

            for i in range(idx, 10):
                if curr + i <= n:
                    path.append(i)
                    backtrack(i+1, curr+i)
                    path.pop()
        path = []
        ans = []
        backtrack(1, 0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    k = 4
    n = 1
    print(sol.combinationSum3(k, n))