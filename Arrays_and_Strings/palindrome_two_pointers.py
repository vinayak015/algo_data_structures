"""
Given a string s, return true if it is a palindrome, false otherwise.
"""

def check_if_palindrome(s):
    right = len(s)-1
    left = 0
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(check_if_palindrome("racecar"))
print(check_if_palindrome("abcdcba"))