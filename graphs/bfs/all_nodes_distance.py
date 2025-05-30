"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

"""

from typing import List
from collections import deque, defaultdict
from binary_trees.tree_utils import build_tree, print_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK_adding_parent_node(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        queue = deque([target])
        seen = {target}
        distance = 0

        while queue and distance < k:
            current_length = len(queue)
            for _ in range(current_length):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return [node.val for node in queue]

    def distanceK_equivalent_graph_bfs(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(curr, parent):
            if curr and parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            if curr.left:
                build_graph(curr.left, curr)
            if curr.right:
                build_graph(curr.right, curr)
        build_graph(root, None)
        ans = []
        seen = {target.val}
        queue = deque([(target.val, 0)])

        while queue:
            cur, distance = queue.popleft()
            if distance == k:
                ans.append(cur)
                continue

            for neighbor in graph[cur]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return ans

    def distanceK_equivalent_graph_dfs(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(curr, parent):
            if curr and parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            if curr.left:
                build_graph(curr.left, curr)
            if curr.right:
                build_graph(curr.right, curr)
        build_graph(root, None)

        ans = []
        seen = {target.val}

        def dfs(curr, distance):
            if distance == k:
                ans.append(curr)
                return
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor, distance+1)
        dfs(target.val, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    target = 5
    k = 2
    root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    print(sol.distanceK_equivalent_graph(root))



