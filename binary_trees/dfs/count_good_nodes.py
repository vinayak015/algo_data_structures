"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

from binary_trees.tree_utils import build_tree, print_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            left = dfs(node.left, max(max_so_far, node.val))
            right = dfs(node.right, max(max_so_far, node.val))
            ans = left + right
            if node.val >= max_so_far:
                ans += 1
            return ans
        return dfs(root, float("-inf"))

    def good_nodes_iter(self, root):
        if not root:
            return 0
        stack = [(root, float("-inf"))]
        ans = 0
        while stack:
            node, max_so_far = stack.pop()
            if node.val >= max_so_far:
                ans += 1
            max_so_far = max(max_so_far, node.val)
            if node.left:
                stack.append((node.left, max_so_far))
            if node.right:
                stack.append((node.right, max_so_far))
        return ans





if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    # root = build_tree([0, 1, 2, 3, 4, None, 5, None, None, None, None, None, None, None, 6])
    print_tree(root)
    print(sol.goodNodes(root))
    print(sol.good_nodes_iter(root))