class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        temp = x
        while temp > 0:
            remainder = temp % 10
            reverse = reverse * 10 + remainder
            temp = temp // 10
        if x == reverse:
            return True
        return False

print(Solution().isPalindrome(0)) # True