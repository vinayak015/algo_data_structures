"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n  # Stores indegree of nodes, each index is a node
        for _, y in edges:
            indegree[y] += 1
        return [idx for idx in range(n) if indegree[idx] == 0]

if __name__ == "__main__":
    edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    sol = Solution()
    print(sol.findSmallestSetOfVertices(6, edges))
