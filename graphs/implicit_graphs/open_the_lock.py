"""
Q752
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.

The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

"""

from typing import List
from collections import deque, defaultdict

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            n = len(target)
            ans = []
            for i in range(n):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i+1:])
            return ans

        seen = set(deadends)
        if "0000" in seen:
            return -1
        queue = deque([("0000", 0)])
        seen.add("0000")

        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps

            for neighbor in neighbors(node):
                if neighbor not in seen:
                    queue.append((neighbor, steps + 1))
                    seen.add(neighbor)
        return -1


if __name__ == "__main__":
    sol = Solution()
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    print(sol.openLock(deadends, target))