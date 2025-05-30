class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if len(s) == 1:
            return s
        ascii_english = {**{idx: chr(idx) for idx in range(65, 91)}, **{idx: chr(idx) for idx in range(97, 123)}}
        reversed = [""]*len(s)
        left = 0
        right = len(s)-1
        while left <= right:
            l_ascii = ord(s[left])
            r_ascii = ord(s[right])
            if l_ascii not in ascii_english:
                reversed[left] = s[left]
                left += 1
            elif r_ascii not in ascii_english:
                reversed[right] = s[right]
                right -= 1
            else:
                reversed[left], reversed[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(reversed)

    def reverseOnlyLetters_2(self, s: str):
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)






s = Solution()
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(s.reverseOnlyLetters_2("Test1ng-Leet=code-Q!"))