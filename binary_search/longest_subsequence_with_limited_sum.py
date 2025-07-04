"""
Q2389
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

"""

from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = [0]*len(queries)
        for i in range(len(queries)):
            max_sum = queries[i]
            curr_sum = 0
            curr_count = 0
            for num in nums:
                curr_sum += num
                if curr_sum <= max_sum:
                    curr_count += 1
            ans[i] = curr_count
        return ans

    def answerQueries_pre_sum_binary_search(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre_sum = [nums[0]]
        for i in range(1, len(nums)):
            pre_sum.append(nums[i] + pre_sum[i-1])
        print(pre_sum)

        def binary_search(arr, query):
            left, right = 0, len(arr)

            while left < right:
                mid = (left + right) // 2
                if query < arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left
        ans = []
        for query in queries:
            ans.append(binary_search(pre_sum, query))
        return ans





if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,2,1]
    queries = [3,10,21]

    # nums = [2, 3, 4, 5]
    # queries = [1]
    print(sol.answerQueries_pre_sum_binary_search(nums, queries))
"""
Time Complexity: 
    m = len(queries)
    n = len(nums)
    sort: O(n.log(n))
    presum: O(n)
    binary_search: O(m.log(n))
    
    Overall: O(n.log(n) + m.log(n)) = O((n + m).log(n))
"""
