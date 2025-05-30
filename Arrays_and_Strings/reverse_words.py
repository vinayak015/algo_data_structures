from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        ans = []

        for i in range(len(split)):
            left = 0
            right = len(split[i]) - 1
            rev = [""]*len(split[i])
            while left <= right:
                rev[right] = split[i][left]
                rev[left] = split[i][right]
                right -= 1
                left += 1
            ans.append("".join(rev))
        return " ".join(ans)

    def reverse_2(self, s: str):
        return " ".join([words[::-1] for words in s.split()])

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverse_2("Let's take LeetCode contest"))