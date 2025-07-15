"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letter_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(curr_idx):
            if curr_idx == len(digits):
                ans.append("".join(path))
                return
            possible_letters = letter_to_char[digits[curr_idx]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(curr_idx + 1)
                path.pop()


        ans = []
        path = []
        backtrack(0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
