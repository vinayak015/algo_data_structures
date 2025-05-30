"""

"""

from typing import List
from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def next_great():
            stack = []
            dic = {}
            for i in range(len(nums2)):
                while stack and nums2[stack[-1]] < nums2[i]:
                    j = stack.pop()
                    dic[nums2[j]] = nums2[i]
                stack.append(i)
            return dic
        mapping = next_great()
        ans = []
        for num in nums1:
            if num in mapping:
                ans.append(mapping[num])
            else:
                ans.append(-1)
        return ans

    def another_sol(self, nums1, nums2):
        stack = []
        hashmap = {}
        for num in nums2:
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)

        while stack:
            hashmap[stack.pop()] = -1

        return [hashmap.get(i, -1) for i in nums1]


if __name__ == "__main__":
    sol = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    # print(sol.nextGreaterElement(nums1, nums2))
    print(sol.another_sol(nums1, nums2))