class Solution_:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left != right and left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -=1
        print(s)

# s = Solution()
# s.reverseString(["H","a","n","n","a","h"])


class Solution:
    def sortedSquares(self, nums) :
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums
        return sorted(nums)

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))


