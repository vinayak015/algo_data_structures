"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""

from typing import Optional, List
from  collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            cur_len = len(queue)
            level_max = float("-inf")

            for _ in range(cur_len):
                node = queue.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_max)
        return ans
