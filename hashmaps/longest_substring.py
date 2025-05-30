"""
Given a string s, find the length of the longest substring without duplicate characters.
"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)

        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            counter[r] += 1

            while counter[r] > 1:
                l = s[left]
                counter[l] -= 1
                left += 1

            res = max(res, right-left+1)

            right += 1
        return res

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        n = len(s)
        ans = 0
        char_to_index = {}
        i = 0
        for j in range(n):
            if s[j] in char_to_index:
                i = max(char_to_index[s[j]], i)

            ans = max(ans, j - i + 1)
            char_to_index[s[j]] = j + 1

        return ans





if __name__ == "__main__":
    s = "abcabcbb"
    s = "abcdeafbdgcbb"
    print(Solution().lengthOfLongestSubstring_2(s))