"""
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
"""

def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    left = 0
    ans = curr
    for right in range(k, len(nums)):
        curr = curr + nums[right] - nums[left] # or, curr + nums[right] - nums[right-k]
        left += 1
        ans = max(ans, curr)
    return ans

print(find_best_subarray([3, -1, 4, 12, -8, 5, 6], 4))