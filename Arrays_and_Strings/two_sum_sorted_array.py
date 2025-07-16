"""
Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""

def check_two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return True
        if target < curr:
            right -= 1
        else:
            left += 1
    return False

print(check_two_sum([1, 2, 4, 6, 8, 9, 14, 15], 20))


"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                break
            if target < curr:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))