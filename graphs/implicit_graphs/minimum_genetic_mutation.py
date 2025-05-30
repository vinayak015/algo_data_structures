"""
Q433
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
"""

from typing import List
from collections import deque

from networkx.classes import neighbors


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        valid_genes = set(bank)
        if endGene not in valid_genes:
            return -1
        if startGene == endGene:
            return 0
        def neighbors(gene):
            adj = {"A": ["C", "G", "T"],
                         "C": ["A", "G", "T"],
                         "G" : ["A", "C", "T"],
                         "T": ["A", "C", "G"]}
            ans = []
            for i in range(len(gene)):
                curr = gene[i]
                for seq in adj[curr]:
                    ans.append(gene[:i] + seq + gene[i+1:])
            return ans

        seen = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene and gene in valid_genes:
                return steps
            for neighbor in neighbors(gene):
                if neighbor not in seen and neighbor in bank: # the mutation will be only valid if it is in the bank
                    seen.add(neighbor)
                    queue.append((neighbor, steps+1))
        return -1

if __name__ == "__main__":
    sol = Solution()
    # startGene = "AACCGGTT"
    # endGene = "AAACGGTA"
    # bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(sol.minMutation(startGene, endGene, bank))

