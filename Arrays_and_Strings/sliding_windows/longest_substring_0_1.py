"""
You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
"""

def find_length(s):
    # This question can be thought of return max subarray with only one "0" in it. Therefore, we can use sliding window
    left, curr, ans = 0, 0, 0

    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left +=1
        ans = max(ans, right - left +1)
    return ans

print(find_length("1101100111"))
