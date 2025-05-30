"""
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.
"""

from typing import List
from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            ans = 1
            seen[node] = True # because I am going to explore the node
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    ans += dfs(neighbor)
            return ans
        seen = [False] * n
        for node in restricted:
            seen[node] = True

        out = dfs(0)
        # print(out)
        return out

    def reachable_nodes(self, n, edges, restricted):
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            ans = 1
            seen.add(node)

            for neighbor in graph[node]:
                if neighbor not in seen:

                    ans += dfs(neighbor)

            return ans


        seen = set()
        for node in restricted:
            seen.add(node)

        ans = dfs(0)
        return ans



if __name__ == "__main__":
    sol = Solution()
    n = 7
    edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted = [4,5]
    print(sol.reachableNodes(n, edges, restricted))
    print(sol.reachable_nodes(n, edges, restricted))


