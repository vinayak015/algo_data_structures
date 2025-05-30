"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def max_depth_iterative(self, root):
        if not root:
            return 0
        stack = [(root,1)]
        ans = 0
        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)

            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return ans




if __name__ == "__main__":
    sol = Solution()
    # root = build_tree([3, 9, 20, None, None, 15, 7])
    root = build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    print_tree(root)

    print(sol.maxDepth(root))
    print(sol.max_depth_iterative(root))
