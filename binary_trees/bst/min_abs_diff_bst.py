"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
"""

from typing import Optional
from binary_trees import tree_utils


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)

        values = []
        dfs(root)
        ans = float("inf")
        for i in range(1, len(values)):
            ans = min(ans, values[i]-values[i-1])
        return ans

if __name__ == "__main__":
    sol = Solution()
    # root = tree_utils.build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    root = tree_utils.build_tree([9, 5, 15, 1, 7])
    tree_utils.print_tree(root)

    print(sol.getMinimumDifference(root))
