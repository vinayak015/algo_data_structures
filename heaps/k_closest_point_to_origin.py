"""
Q973
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist2 = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist2, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point[1] for point in heap]


if __name__ == "__main__":
    sol = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(sol.kClosest(points, k))

"""
Time Complexity:
Given n points, pushing and popping takes: O(n.log(n))
We again iterate the list k times before returning, O(k), in the worst case k=n.
Total Complexity = O(n.log(n) + n) 
"""

