"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.result = 0

        def dfs(node, cur_max, cur_min):
            if not node:
                return
            self.result = max(self.result, abs(node.val - cur_max), abs(node.val - cur_min))
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            dfs(node.left, cur_max, cur_min)
            dfs(node.right, cur_max, cur_min)
        dfs(root, root.val, root.val)
        return self.result

    def maxAncestorDiff_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, cur_max, cur_min):
            if not node:
                return cur_max - cur_min
            cur_max = max(node.val, cur_max)
            cur_min = min(node.val, cur_min)
            left = dfs(node.left, cur_max, cur_min)
            right = dfs(node.right, cur_max, cur_min)
            return max(left, right)
        return dfs(root, root.val, root.val)


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([8,3,10,1,6,None,14,None,None,4,7,13])
    # root = build_tree([3,9,20,None,None,15,7])
    # root = build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    print_tree(root)
    print(sol.maxAncestorDiff_2(root))

