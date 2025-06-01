"""
Q2101
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
"""

from typing import List
from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def cal_distance_squared(x1, x2, y1, y2):
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2)

        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i==j:
                    continue
                xj, yj, rj = bombs[j]
                dist = cal_distance_squared(xi, xj, yi, yj)
                if dist <= ri ** 2:
                    graph[i].append(j)
        def dfs(node):
            curr = 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    curr += dfs(neighbor)
            return curr

        ans = 1
        for i in range(len(bombs)):
            seen = {i}
            ans = max(ans, dfs(i))
        return ans



if __name__ == "__main__":
    sol = Solution()
    bombs = [[2,3,1],[3,4,2],[4,5,3],[5,6,4],[1,2,3],]
    print(sol.maximumDetonation(bombs))
