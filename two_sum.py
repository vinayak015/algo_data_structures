from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {val: idx for idx, val in enumerate(nums)}
        if target > 0 and target % 2 == 0:
            half = target // 2
            if nums.count(half) == 2:
                return [index for index, value in enumerate(nums) if value == half]
        else:
            half = abs(target) // 2
            if nums.count(-half) == 2:
                return [index for index, value in enumerate(nums) if value == -half]

        for num in nums:
            diff = target - num
            if diff in num_to_idx and diff != num:
                return [num_to_idx[num], num_to_idx[diff]]

    def better_twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {v:i for i, v in enumerate(nums)}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_to_idx and num_to_idx[diff]!=i:
                return [i, num_to_idx[diff]]

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 4], 8), [3, 4])
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 10), None)
        self.assertEqual(self.solution.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
        self.assertEqual(self.solution.twoSum([-1, 2, -3, 4, -5], -4), [0, 2])

    def test_better_twoSum(self):
        self.assertEqual(self.solution.better_twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.better_twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.solution.better_twoSum([3, 3], 6), [0, 1])
        self.assertEqual(self.solution.better_twoSum([1, 2, 3, 4, 4], 8), [3, 4])
        self.assertEqual(self.solution.better_twoSum([1, 2, 3, 4, 5], 10), None)
        self.assertEqual(self.solution.better_twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
        self.assertEqual(self.solution.better_twoSum([-1, 2, -3, 4, -5], -4), [0, 2])

if __name__ == '__main__':
    unittest.main()