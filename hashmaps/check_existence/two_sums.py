"""
Two Sums: Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        return [-1, -1]


    def repeatedCharacter(self, s: str) -> str:
        """
        Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character
        :param s:
        :return:
        """
        until_now = set()
        for string in s:
            if string not in until_now:
                until_now.add(string)
            else:
                return string

    def find_numbers(self, nums):
        """
        Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
        :param nums:
        :return:
        """
        all_nums = set(nums)
        uniques = []

        for num in nums:
            if num + 1 in all_nums and num - 1 in all_nums:
                uniques.append(num)
        return uniques


if __name__ == "__main__":
    s = Solution()
    nums = [5, 2, 7, 10, 3, 9]
    target = 14
    print(s.twoSum(nums, target))

    chars = "abcdeda"
    print(s.repeatedCharacter(chars))

    unq_test = [5, 2, 4, 10, 3, 9]
    print(s.find_numbers(unq_test))