"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
    def practice(self, temps):
        stack = []
        mapping = {}
        for temp in temps:
            while stack and stack[-1] < temp:
                mapping[stack.pop()] = temp
            stack.append(temp)
        print(mapping)
        print()

    def practice_daily_temp(self, temps):
        stack = []
        ans = [0] * len(temps)
        for i in range(len(temps)):
            while stack and temps[stack[-1]] < temps[i]:
                j = stack.pop()
                diff = i - j
                ans[j] = diff
            stack.append(i)
        print(ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    temps = [40, 35, 32, 37, 50]
    print(temps)
    # print(sol.dailyTemperatures(temps))
    # print(sol.practice(temps))
    print(sol.practice_daily_temp(temps))