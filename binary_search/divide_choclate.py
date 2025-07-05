"""
Q1231
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
"""

from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        no_of_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // no_of_people

        while left < right:
            mid = (left + right + 1) // 2
            curr_sweetness = 0
            people_with_chocolate = 0

            for s in sweetness:
                curr_sweetness += s
                if curr_sweetness >= mid:
                    people_with_chocolate += 1
                    curr_sweetness = 0

            if people_with_chocolate >= no_of_people:
                left = mid
            else:
                right = mid - 1

        return right


if __name__ == "__main__":
    sol = Solution()
    sweetness = [1,2,3,4,5,6,7,8,9]
    k = 5
    print(sol.maximizeSweetness(sweetness, k))

"""
Time Complexity: 
    m = sum(sweetness) // (k+1), n = len(sweetness)
    Overall Complexity: O(n.log(m))
"""