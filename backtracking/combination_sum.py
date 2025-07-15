"""
Given an array of distinct positive integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, curr):
            if curr == target:
                ans.append(path[:])
                return

            for j in range(idx, len(candidates)):
                if curr + candidates[j] <= target:
                    path.append(candidates[j])
                    backtrack(j, curr + candidates[j])
                    path.pop()


        ans = []
        curr = 0
        path = []
        backtrack(0, curr)
        return ans


if __name__ == "__main__":
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(sol.combinationSum(candidates, target))