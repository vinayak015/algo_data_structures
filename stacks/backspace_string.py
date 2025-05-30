"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".
"""

class Solution:
    def backspace_compare(self, s: str, t: str) -> bool:

        def build_chars(s):
            stack = []
            for char in s:
                if char == "#":
                    if stack:
                        stack.pop()
                    else:
                        continue
                else:
                    stack.append(char)
            return stack


        if "".join(build_chars(s)) == "".join(build_chars(t)):
            return True
        return False




if __name__ == "__main__":
    sol = Solution()
    print(sol.backspace_compare("ab#c", "ad#c"))