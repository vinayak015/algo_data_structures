"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""

from typing import List
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        ans = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                ans += 1
                seen.add(node)
                dfs(node)

        return ans

if __name__ == "__main__":
    sol = Solution()
    n = 4
    edges = [[2,3],[1,2],[1,3]]
    print(sol.countComponents(n, edges))