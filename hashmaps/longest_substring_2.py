"""
Given a string s, find the length of the longest substring without duplicate characters.
"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_idx = defaultdict(int)
        i = 0
        n = len(s)
        ans = 0

        for j in range(n):
            if s[j] in char_to_idx:
                i = max(i, char_to_idx[s[j]])

            ans = max(ans, j-i+1)
            char_to_idx[s[j]] = j+1
        return ans

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        freq_map = defaultdict(int)
        left = right = 0
        ans = 0
        while right < len(s):
            freq_map[s[right]] += 1

            while freq_map[s[right]] > 1:
                freq_map[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans


if __name__ == "__main__":
    # s = "abcabcbb"
    s = "abcdeafbdgcbb"
    print(Solution().lengthOfLongestSubstring_2(s))