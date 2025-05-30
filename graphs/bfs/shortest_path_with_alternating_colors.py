"""
Q1129
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

"""

from collections import deque, defaultdict
from typing import List


class Solution:
    def shortestAlternatingPaths_(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = 0
        blue = 1
        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[red][x].append(y)
        for x, y in blueEdges:
            graph[blue][x].append(y)

        seen = [(0, red), (0, blue)]
        queue = deque([(0, red, 0), (0, blue, 0)])
        ans = [float("inf")] * n

        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)
            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    # seen.add((neighbor, 1-color))
                    seen.append((neighbor, 1-color))
                    queue.append((neighbor, 1 - color, steps + 1))

        return [ans_ if ans_!=float("inf") else -1 for ans_ in ans]

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = 0
        blue = 1
        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[red][x].append(y)

        for x, y in blueEdges:
            graph[blue][x].append(y)

        seen = {(0, red), (0, blue)}
        queue = deque([(0, red, 0), (0, blue, 0)])
        ans = [float("inf")] * n

        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)

            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1 - color))
                    queue.append((neighbor, 1 - color, steps + 1))
        return [ans_ if ans_ != float("inf") else -1 for ans_ in ans]




if __name__ == "__main__":
    sol = Solution()
    r = [[0,1], [2, 3], [1, 5]]
    b = [[1, 2], [3,4]]

    print(sol.shortestAlternatingPaths(6, r, b))