"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import defaultdict

class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        magazine_dict = defaultdict(int)
        for char in magazine:
            magazine_dict[char] += 1

        can_be_constructed = False

        for char in ransom_note:
            magazine_dict[char] -= 1
            if magazine_dict[char] >= 0:
                can_be_constructed = True
            else:
                return False

        return can_be_constructed


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "ab"
    print(Solution().can_construct(ransomNote, magazine))
