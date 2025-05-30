"""
Q399
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
"""

from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def answer_query(num, den):
            if num not in graph:
                return -1
            seen = {num}
            stack = [(num, 1)]

            while stack:
                node, mult = stack.pop()
                if node == den:
                    return mult
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, mult * graph[node][neighbor]))
            return -1


        graph = defaultdict(dict)
        for i in range(len(equations)):
            num, den = equations[i]
            val = values[i]
            graph[num][den] = val
            graph[den][num] = 1. / val

        ans = []
        for num, den in queries:
            ans.append(answer_query(num, den))

        return ans



if __name__ == "__main__":
    sol = Solution()
    equations = [["a", "b"], ["b", "d"],  ["b", "c"]]
    values = [2.0, 4.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(sol.calcEquation(equations, values, queries))

