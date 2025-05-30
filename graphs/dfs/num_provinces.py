"""
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                # to prevent cycles
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)


        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        return ans

if __name__ == "__main__":
    sol = Solution()
    is_connected = [[1,1,0],[1,1,0],[0,0,1]]
    print(sol.findCircleNum(is_connected))