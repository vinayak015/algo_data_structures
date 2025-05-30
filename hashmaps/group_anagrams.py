"""
Given an array of strings strs, group the anagrams together.

For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].
"""

from collections import defaultdict
from typing import List

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            hashmap[key].append(str)

        return list(hashmap.values())


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().group_anagrams(strs))
