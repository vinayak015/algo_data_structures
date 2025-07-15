"""
Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.
"""

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        def dfs(n, num):
            if n == 0:
                ans.append(num)
                return

            last_digit = num % 10
            possible_nums = set([last_digit + k, last_digit - k])
            for possible_num in possible_nums:
                if 0 <= possible_num < 10:
                    new_num = num * 10 + possible_num
                    dfs(n-1, new_num)

        ans = []
        for i in range(1, 10):
            dfs(n-1, i)

        return ans

if __name__ == "__main__":
    sol = Solution()
    n = 3
    k = 2
    print(sol.numsSameConsecDiff(n, k))