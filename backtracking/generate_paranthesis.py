"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, left, right):
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return
            if left < n:
                curr.append("(")
                backtrack(curr, left + 1, right)
                curr.pop()
            if right < left:
                curr.append(")")
                backtrack(curr, left, right + 1)
                curr.pop()
        ans = []
        backtrack([], 0, 0)
        return ans



if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.generateParenthesis(n))