"""
Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.
"""

from collections import defaultdict
from typing import List


class Solution:
    def min_card_pickup(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        min_ = float("inf")
        for i, num in enumerate(nums):
           if num in hashmap:
               min_ = min(min_, i - hashmap[num] + 1)
           hashmap[num] = i
        return min_ if min_ < float("inf") else -1

    def min_card_pickup_2(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        for i, num in enumerate(nums):
            hashmap[num].append(i)

        min_ = float("inf")
        for val in hashmap.values():
            for i in range(0, len(val) -1):
                min_ = min(min_, val[i+1] - val[i] + 1 )
        return min_ if min_ < float("inf") else -1


if __name__ == "__main__":
    cards = [1, 2, 6, 2, 1 ]
    print(Solution().min_card_pickup_2(cards))

