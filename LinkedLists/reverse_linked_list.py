from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev





if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    sol = Solution()
    reversed_head = sol.reverse_list(head)
    while reversed_head:
        val = reversed_head.val
        print(val)
        reversed_head = reversed_head.next

    print()
