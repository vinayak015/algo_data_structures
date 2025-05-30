from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        window_size = 2 * k + 1
        n = len(nums)
        avgs = [-1] * n

        if window_size > n:
            return avgs

        prefix = [0]
        for i in range(n):
            prefix.append(nums[i] + prefix[i])

        for i in range(k, n-k):
            left = i - k
            right = i + k

            sub_sum = prefix[right + 1] - prefix[left]
            avgs[i] = sub_sum // window_size
        return avgs

    def getAverages_sliding_window(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        window_size = 2*k + 1
        n = len(nums)
        avgs = [-1] * n
        if window_size > n:
            return avgs

        window_sum = sum(nums[:window_size])
        avgs[k] = window_sum // window_size

        for i in range(window_size, n):
            window_sum = window_sum + nums[i] - nums[i - window_size]
            avgs[i - k] = window_sum // window_size

        return avgs



s = Solution()
print(s.getAverages([7,4,3,9,1,8,5,2,6], k = 3))
print(s.getAverages_sliding_window([7,4,3,9,1,8,5,2,6], k = 3))