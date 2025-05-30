"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
"""


from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        unq = set(arr)
        count = 0
        for i in arr:
            if i+1 in unq:
                count+=1
        return count

if __name__=="__main__":
    arr = [1,3,2,3,5,0]
    sol = Solution()
    count = sol.countElements(arr)
    print(count)