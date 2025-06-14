"""
Q881
You are given an array people where people[i] is the weight of the ith person.
A boat can hold up to two people, if their weight combined is less than or equal to limit.
What is the fewest number of boats you need to carry everyone? Note: no person is heavier than limit.
"""

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        people.sort()
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.numRescueBoats([3,2,2,1], 3))

"""
Time Complexity:
for sorting: O(n.log(n))
while loop: O(n)
Therefore, overall complexity: O(n.log(n))
"""