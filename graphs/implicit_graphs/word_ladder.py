"""
Q127
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""


from typing import List
from collections import deque, defaultdict
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        chars = set(string.ascii_lowercase)
        valid_words = set(wordList)
        if endWord not in valid_words:
            return 0
        def neighbors(node):
            ans = set()
            for i in range(len(node)):
                for char in chars:
                    new_word = node[:i] + char + node[i+1:]
                    if new_word in valid_words:
                        ans.add(new_word)
            return ans
        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            node, steps = queue.popleft()
            if node == endWord:
                return steps
            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))
        return 0

    def ladderLength_improved(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        valid_words = set(wordList)
        if endWord not in valid_words:
            return 0
        graph = defaultdict(list)
        def create_graph():
            for word in wordList:
                for i in range(len(word)):
                    graph[word[:i] + "*" + word[i+1:]].append(word)
        create_graph()
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        seen_transition = set()

        while queue:
            node, steps = queue.popleft()
            if node == endWord:
                return steps
            transitions = {node[:i] + "*" + node[i+1:] for i in range(len(node))}
            for transition in transitions:
                if transition in seen_transition:
                    continue
                seen_transition.add(transition)
                for neighbor in graph[transition]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return 0



if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # print(sol.ladderLength(beginWord, endWord, wordList))
    print(sol.ladderLength_improved(beginWord, endWord, wordList))


"""
Time Complexity:
Building the graph takes O(N.M**2), where M=len(word) and N=len(wordList). 
In BFS each transition pattern is scanned once, creating the transition O(M**2) and the iteration will be N times.
Therefore, for DFS it will be O(N.M**2) as well. Hence, the total time complexity: O(N.M**2)

Space Complexity:
O(MN) for creating dict, but len(word) is M -> O(N.M**2)
"""