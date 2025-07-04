"""
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.


"""

from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # if num of trains are more than integer num of hours then it is not possible to reach office
        if len(dist) > math.ceil(hour):
            return -1

        def check(speed):
            total = 0
            for d in dist:
                total = math.ceil(total)
                total += (d / speed)
            return total <= hour

        left, right = 1, 10 ** 7

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    sol = Solution()
    dist = [5,3,4,6,2,2,7]
    hour = 10.93
    print(sol.minSpeedOnTime(dist, hour))

"""
Time Complexity:
    m, n = len(heights), len(heights[0])
    k = max(heights)
    DFS: O(m.n)
    binary_search: O(log(k))

    Overall Complexity: O(m.n.log(k))
"""




