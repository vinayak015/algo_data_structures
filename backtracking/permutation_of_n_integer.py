"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List

class Solution:
    def permute_(self, nums: List[int]) -> List[List[int]]:
        def perm(k):
            if k == len(nums):
                ans.append(res[:])
                return
            for i in range(len(nums)):
                print(i, k)
                if not seen[i]:
                    res[k] = nums[i]
                    seen[i] = True
                    perm(k + 1)
                    seen[i] = False

        seen = [False] * len(nums)
        res = [None] * len(nums)
        ans = []
        perm(0)
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        curr = []
        backtrack(curr)
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute_(nums))
