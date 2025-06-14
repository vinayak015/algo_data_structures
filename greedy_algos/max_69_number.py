"""
Q1323
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)
        ans = num
        for i in range(len(num_str)):
            curr = num_str[i]
            if curr == "6":
                curr = "9"
                curr_num = int(num_str[:i] + curr + num_str[i + 1:])
                ans = max(ans, curr_num)
                break

        return ans

if __name__ == "__main__":
    sol = Solution()
    num = 9996
    print(sol.maximum69Number(num))

"""
Time Complexity:
O(n), because the loop breaks after concatenating the string and concat takes O(n), where n = len(str(num)) 
"""