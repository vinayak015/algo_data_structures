"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        curr, prev = head, None
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1

        cond, tail = prev, curr
        while right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            right -= 1

        if cond:
            cond.next = prev
        else:
            head = prev
        tail.next = curr

        return head







if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))

    sol = Solution()
    reversed_head = sol.reverseBetween(head, 3, 5)
    while reversed_head:
        print(reversed_head.val)
        reversed_head = reversed_head.next

