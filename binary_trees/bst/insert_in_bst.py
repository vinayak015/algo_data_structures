"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root

if __name__ == "__main__":
    sol = Solution()
    # root = tree_utils.build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    root = tree_utils.build_tree([9, 5, 15, 1, 7])
    tree_utils.print_tree(root)

    new_root = sol.insertIntoBST(root, 8)

    tree_utils.print_tree(new_root)




