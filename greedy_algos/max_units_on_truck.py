"""
Q1710
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""

from typing import List
import heapq


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = [(-j, i) for i, j in boxTypes]
        heapq.heapify(heap)
        ans = 0
        while truckSize != 0 and heap:
            units, boxes = heapq.heappop(heap)
            box_count = min(truckSize, boxes)
            truckSize = truckSize - box_count
            push_to_truck = -units * box_count
            ans += push_to_truck

        return ans

    def maximumUnits_sol2(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        unitCount = 0
        for boxType in boxTypes:
            boxCount = min(truckSize, boxType[0])
            unitCount += boxCount * boxType[1]
            truckSize -= boxCount
            if truckSize == 0:
                break
        return unitCount



if __name__ == "__main__":
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    sol = Solution()
    print(sol.maximumUnits_sol2(boxTypes, truckSize))

"""
Time Complexity:
1. Heap Method:
    heapify: O(n)
    while loop: O(n)
        popping: log(n)
    Overall: O(n) + O(n + n.log(n)) = O(n.log(n))

2. Sorting: 
    Sort: O(n.log(n))
    for loop: O(n)
    Overall: O(n.log(n)) + O(n) = O(n.log(n))
"""
