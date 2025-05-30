"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.

For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.
"""

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        matching = {"(" : ")",
                    "{" : "}",
                    "[" : "]"
                    }

        for char in s:
            if char in matching:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_opening = stack.pop()
                if matching[last_opening] != char:
                    return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_valid("(){}[]"))
