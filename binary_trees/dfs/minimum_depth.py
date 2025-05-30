"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([2,None,3,None,4,None,5,None,6])
    root = build_tree([3,9,20,None,None,15,7])
    # root = build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    print_tree(root)
    print(sol.minDepth(root))