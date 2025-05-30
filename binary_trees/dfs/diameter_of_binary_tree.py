"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter = 0
        def dfs(node, ):
            if not node:
                return 0
            nonlocal diameter
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        dfs(root)
        return diameter

if __name__ == "__main__":
    sol = Solution()
    root = build_tree([8,3,10,1,6,None,14,None,None,4,7,13])
    # root = build_tree([1,2])
    # root = build_tree([3,9,20,None,None,15,7])
    # root = build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    print_tree(root)
    print(sol.diameterOfBinaryTree(root))

