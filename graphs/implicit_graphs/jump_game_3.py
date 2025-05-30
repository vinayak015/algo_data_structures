"""
Q1306
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = dict()
        n = len(arr)
        for i in range(n):
            valid_jumps = []
            if arr[i] == 0:
                valid_jumps.append(None)
                graph[i] = valid_jumps
                continue
            if i+arr[i] < n:
                valid_jumps.append(i+arr[i])
            if i - arr[i] > -1:
                valid_jumps.append(i - arr[i])
            graph[i] = valid_jumps

        seen = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor is None:
                    return True
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False

    def can_reach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        # seen = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue
            for jump in [node+arr[node], node-arr[node]]:
                if 0 <= jump < n:
                    queue.append(jump)
            # seen.add(jump)
            arr[node] = -arr[node]
        return False


if __name__ == "__main__":
    sol = Solution()
    arr = [3,0,2,1,2]
    start = 2
    print(sol.canReach(arr, start))
    print(sol.can_reach(arr, start))
