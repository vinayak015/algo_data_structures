"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def backtrack(curr_node, path):
            if curr_node == target:
                results.append(path[:])
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = [0]
        backtrack(0, path)
        return results

if __name__ == "__main__":
    sol = Solution()
    graph = [[1,2],[3],[3],[]]
    print(sol.allPathsSourceTarget(graph))
