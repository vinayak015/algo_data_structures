"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.
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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node, closest):
            if not node:
                return closest
            closest = min(node.val, closest, key= lambda x:(abs(x-target), x))
            branch = node.left if target < node.val else node.right
            return dfs(branch, closest)
        return dfs(root, root.val)

if __name__ == "__main__":
    sol = Solution()
    # root = tree_utils.build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    root = tree_utils.build_tree([4,2,5,1,3])
    tree_utils.print_tree(root)

    print(sol.closestValue(root, 4.5))
    # print(sol.closestValue_2(root, 5.9))
