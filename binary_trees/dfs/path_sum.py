"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

from typing import Optional
from binary_trees.tree_utils import build_tree, print_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            if node.left is None and node.right is None:
                return (curr + node.val) == targetSum

            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right

        return dfs(root, 0)

if __name__ == "__main__":
    sol = Solution()
    # root = build_tree([3, 9, 20, None, None, 15, 7])
    root = build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    print_tree(root)
    print(sol.hasPathSum(root, 7))