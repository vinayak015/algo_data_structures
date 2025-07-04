"""
You are given two positive integer arrays spells and potions, where spells[i] represents the strength of the i_th spell and potions[j] represents the strength of the j_th potion.
You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success. For each spell, find how many potions it can pair with to be successful.
Return an integer array where the i_th element is the answer for the i_th spell.
"""

from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, key):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if key <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left

        potions.sort()
        ans = [0] * len(spells)
        for i in range(len(spells)):
            f = success / spells[i]
            left_idx = binary_search(potions, f)
            ans[i] = len(potions) - left_idx
        return ans

if __name__ == "__main__":
    sol = Solution()
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16

    print(sol.successfulPairs(spells, potions, success))

"""
Time complexity:
    Let m = len(potions), n = len(spells)
    sorting potions = O(m.log(m))
    for loop + binary search = O(n.log(m))
    Total complexity = O((m+n).log(m))
"""