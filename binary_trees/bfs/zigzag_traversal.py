"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        order = True
        while queue:
            cur_len = len(queue)
            cur_level = [None] * cur_len
            for i in range(cur_len):
                node = queue.popleft()
                if order:
                    cur_level[i] = node.val
                else:
                    cur_level[cur_len-i-1] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            order = not order
            ans.append(cur_level)
        return ans


