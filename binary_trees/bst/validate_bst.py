"""
Given the root of a binary tree, determine if it is a valid BST.
"""

from binary_trees import tree_utils
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True
            if not (small < node.val < large):
                return False
            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)
            return left and right
        return dfs(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    sol = Solution()
    # root = tree_utils.build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    root = tree_utils.build_tree([9, 5, 15, 1, 7])
    tree_utils.print_tree(root)

    print(sol.isValidBST(root))