"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        
        while left < right:
            s[left], s[right] = s[right], s[left]

            right -= 1
            left += 1

        print(s)

if __name__ == "__main__":
    Solution().reverseString(["H", "e", "l", "l", "o"])