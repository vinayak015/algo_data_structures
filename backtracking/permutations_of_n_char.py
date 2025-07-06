"""
1. Given a string, print it's all permutations
2. Given a string, print it's all permutations, given no two consecutive chars should be together
"""


class Solution:
    def find_permutations(self, string: str):
        res = [None] * len(string)
        seen = [False] * len(string)

        def perm(k):
            if k == len(string):
                print("".join(res))
                return
            for i in range(len(string)):
                if not seen[i]:
                    res[k] = string[i]
                    seen[i] = True
                    perm(k+1)
                    seen[i] = False
        perm(0)

    def find_permutations_no_consecutive(self, string: str):
        res = [None] * len(string)
        seen = [False] * len(string)

        def perm(k):
            if k == len(string):
                print("".join(res))
                return
            for i in range(len(string)):
                if not seen[i]:
                    if k > 0 and ord(string[i]) - ord(string[k - 1]) == 1:
                        continue
                    res[k] = string[i]
                    seen[i] = True
                    perm(k+1)
                    seen[i] = False
        perm(0)

if __name__ == "__main__":
    sol = Solution()
    string = "ABC"
    print(sol.find_permutations(string))
    print(sol.find_permutations_no_consecutive(string))

"""
Time complexity: n! but asymptotically it is O(n**n)
"""

