"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.
"""

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        def dp(i, rem):
            if i == len(piles) or rem == 0:
                return 0
            ans = dp(i+1, rem)
            curr = 0
            for j in range(min(rem, len(piles[i]))):
                curr += piles[i][j]
                ans = max(ans, curr + dp(i+1, rem-j-1))

            return ans
        return dp(0, k)

if __name__ == "__main__":
    sol = Solution()
    piles =  [[1,100,3],[7,8,9]]
    piles =  [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
    print(sum(sum(pile) for pile in piles))
    k = 2
    k = 7
    print(sol.maxValueOfCoins(piles, k))