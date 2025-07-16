"""
 Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.
"""

def find_length(nums, k):
    left = 0
    curr = 0
    ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans

print(find_length([3, 2, 1, 3, 1, 1], 6))