"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        ans = 0
        if low <= root.val <= high:
            ans += root.val
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)
        if high > root.val:
            ans += self.rangeSumBST(root.right, low, high)

        return ans

    def rangeSum_iter(self, root, low, high):
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if low <= node.val <=  high:
                ans += node.val
            if node.left and low < node.val:
                stack.append(node.left)
            if node.right and high > node.val:
                stack.append(node.right)
        return ans


if __name__ == "__main__":
    sol = Solution()
    # root = tree_utils.build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    root = tree_utils.build_tree([10, 5, 15, 3, 7, None, 18])
    tree_utils.print_tree(root)

    print(sol.rangeSumBST(root, 7, 15))