"""
Given the head of a linked list, swap every pair of nodes. For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6, return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = head.next
        prev = None
        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head

            next_node = head.next.next
            head.next.next = head
            head.next = next_node
            head = next_node
        return dummy


if __name__ == "__main__":
    head = ListNode("A", ListNode("B", ListNode("C", ListNode("D", ListNode("E", ListNode("F"))))))

    reversed_pairs = Solution().swapPairs(head)
    while reversed_pairs:
        print(reversed_pairs.val)
        reversed_pairs = reversed_pairs.next
