"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1) + 1
            else:
                return max(dp(i-1, j), dp(i, j-1))
        return dp(len(text1)-1, len(text2)-1)

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))
