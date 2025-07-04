"""
Q875
Koko loves to eat bananas. There are n piles of bananas, the i_th pile has piles[i] bananas. Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses a pile and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them and will not eat any more bananas during the hour.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""


from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)

            return hours <= h

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()
    piles = [3,6,7,11]
    h = 8

    print(sol.minEatingSpeed(piles, h))
"""
Time Complexity: O(log(n))
"""